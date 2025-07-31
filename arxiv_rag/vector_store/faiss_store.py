import faiss
import numpy as np
from typing import List, Dict
from arxiv_rag.vector_store.embeddings import EmbeddingModel

class VectorStore:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        self.embedding_model = EmbeddingModel(model_name)
        self.index = None
        self.documents = []
    
    def chunk_text(self, text: str, chunk_size: int = 500, chunk_overlap: int = 50) -> List[str]:
        from langchain.text_splitter import RecursiveCharacterTextSplitter
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        return splitter.split_text(text)
    
    def create_index(self, documents: List[str]):
        self.documents = documents
        embeddings = self.embedding_model.embed_documents(documents)
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)
    
    def search(self, query: str, k: int = 3) -> List[Dict]:
        query_embedding = self.embedding_model.embed_query(query)
        distances, indices = self.index.search(np.array([query_embedding]), k)
        
        results = []
        for idx, distance in zip(indices[0], distances[0]):
            if idx >= 0:
                results.append({
                    "document": self.documents[idx],
                    "score": float(distance)
                })
        return results