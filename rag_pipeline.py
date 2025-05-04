from retrieval import Retriever
from generation import Generator

generator = Generator(model_name="llama3")
retriever = Retriever()

def get_top_k_docs(query, k=3):
    return retriever.retrieve(query, top_k=k)

def rag_respond(query, k=3):
    """
    Full RAG pipeline:
    1. Retrieve top-k documents related to the query
    2. Generate an answer based on the retrieved context
    """
    context = get_top_k_docs(query, k=k)
    answer = generator.generate_answer(query, context)
    return answer