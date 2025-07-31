# run_rag.py

from arxiv_rag.llm.local_llm import OpenSourceLLM
from arxiv_rag.retrieval.arxiv_retriever import ArXivRetriever

llm = OpenSourceLLM()
retriever = ArXivRetriever()

def answer_question_with_rag(question: str) -> str:
    """
    Answer a question using retrieved context from arXiv and a local LLM.
    """
    if not question.strip():
        return "Please enter a valid question."

    # Retrieve relevant context
    context = retriever.process_query(user_query=question)

    # Generate answer using local LLM
    answer = llm.generate_response(
        question=question,
        context=context
    )
    return answer


# Allow CLI execution too
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please provide a question as an argument.")
    else:
        question = " ".join(sys.argv[1:])
        print("Answer:\n", answer_question_with_rag(question))
