import arxiv
from PyPDF2 import PdfReader
import requests
import os

from .pdf_processor import PDFProcessor

class ArXivRetriever:
    def __init__(self, max_results: int = 5, download_dir: str = "papers"):
        self.max_results = max_results
        self.download_dir = download_dir
        self.pdf_processor = PDFProcessor()
        os.makedirs(download_dir, exist_ok=True)

    def search_papers(self, query: str = None, paper_ids: list = None) -> list:
        """Search by query or by specific paper IDs"""
        client = arxiv.Client()
        if paper_ids:
            return list(client.results(arxiv.Search(id_list=paper_ids)))
        return list(client.results(
            arxiv.Search(
                query=query,
                max_results=self.max_results,
                sort_by=arxiv.SortCriterion.Relevance
            )
        ))

    def process_query(self, user_query: str = None, paper_ids: list = None) -> str:
        """Process either a search query or specific paper IDs"""
        if not any([user_query, paper_ids]):
            raise ValueError("Either user_query or paper_ids must be provided")
            
        papers = self.search_papers(query=user_query, paper_ids=paper_ids)
        all_text = ""
        
        for paper in papers:
            try:
                filename = f"{paper.get_short_id()}.pdf"
                pdf_path = os.path.join(self.download_dir, filename)
                if not os.path.exists(pdf_path):
                    response = requests.get(paper.pdf_url)
                    with open(pdf_path, 'wb') as f:
                        f.write(response.content)
                text = self.pdf_processor.extract_text(pdf_path)
                all_text += f"Paper Title: {paper.title}\n\n{text}\n\n"
            except Exception as e:
                print(f"Error processing {paper.title}: {e}")
        return all_text