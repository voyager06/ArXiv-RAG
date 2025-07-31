from typing import List
from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingModel:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
    
    def embed_documents(self, documents: List[str]) -> np.ndarray:
        return self.model.encode(documents)
    
    def embed_query(self, query: str) -> np.ndarray:
        return self.model.encode(query)