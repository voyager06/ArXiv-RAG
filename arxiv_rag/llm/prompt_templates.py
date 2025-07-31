PROMPT_TEMPLATES = {
    "default": """<|system|>
    You are a research assistant. Answer concisely.</s>
    <|user|>
    Question: {question}
    Context: {context}</s>
    <|assistant|>
    """,
    
    "summarize": """<|system|>
    Summarize the key points from these papers.</s>
    <|user|>
    Papers: {context}</s>
    <|assistant|>
    Summary:"""
}