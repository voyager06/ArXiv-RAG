🧠 ArXiv-RAG: Semantic Research Paper Q&A using RAG + LLMs

Semantic Retrieval + LLM-powered Question Answering over ArXiv research papers.

✨ Features
🔍 Semantic Search over academic PDFs using OpenAI embeddings

📚 PDF Parsing + Chunking for efficient document ingestion

⚙️ FAISS Vector Store for fast and accurate similarity search

💬 RAG Pipeline with LangChain to enable contextual question answering

🧪 Streamlit Frontend for live Q&A interaction

🧠 Handles long documents and multi-section academic text
<img width="1598" height="668" alt="Screenshot 2025-08-05 105054" src="https://github.com/user-attachments/assets/20b6e087-40f1-4b57-80fb-2e321fecd55d" />

| Component     | Tool/Library       |
| ------------- | ------------------ |
| Embeddings    | `OpenAIEmbeddings` |
| Retriever     | `FAISS`            |
| PDF Parsing   | `PyMuPDF (fitz)`   |
| LLM           | `OpenAI GPT-3.5`   |
| RAG Framework | `LangChain`        |
| Interface     | `Streamlit`        |
| Vector DB     | `FAISS`            |


🧪 How It Works
PDF documents are parsed and split into semantic chunks (~500 tokens).

Each chunk is embedded using OpenAI’s text-embedding-ada-002.

All embeddings are stored in a FAISS vector store.

When a question is asked:

Relevant chunks are retrieved using vector similarity.

A prompt is constructed with context + question.

An LLM generates the final answer.

Results are displayed instantly via Streamlit UI.

