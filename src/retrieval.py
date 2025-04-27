# file goal: when the user runs the script, it should search through our docs elbeddings and retirieve the most similar to user query
"""
1. building faiss index from the embeddings
2. embed user query
3. search faiss index for top matches
4. return best doc
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from src.embeddings import load_documents, embed_documents

class Retriever:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.documents = load_documents()
        self.embeddings = embed_documents(self.documents, model_name)
        
        dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(np.array(self.embeddings))

    def retrieve(self, query, top_k=1):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_embedding), top_k)
        
        retrieved_docs = [self.documents[idx] for idx in indices[0]]
        return retrieved_docs

if __name__ == "__main__":
    retriever = Retriever()
    query = input("Enter your query: ")
    results = retriever.retrieve(query, top_k=1)
    print("\nTop result:")
    print(results[0])