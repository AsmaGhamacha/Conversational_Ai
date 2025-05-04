# file goal: when the user runs the script, it should search through our docs elbeddings and retirieve the most similar to user query
"""
1.load/compute embeddings for documents
2. building faiss index from the embeddings
3. embed user query
4. search faiss index for top matches
5. return best doc
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from src.embeddings import load_documents, embed_documents
import json

CACHE_DIR = "cached"
EMBEDDINGS_FILE = os.path.join(CACHE_DIR, "embeddings.npy")
DOCUMENTS_FILE = os.path.join(CACHE_DIR, "documents.jsonl")

class Retriever:
    def __init__(self, model_name='thenlper/gte-small'):
        self.model = SentenceTransformer(model_name)

        if os.path.exists(EMBEDDINGS_FILE) and os.path.exists(DOCUMENTS_FILE):
            print("[INFO] Loading cached embeddings and documents (.jsonl)...")
            self.embeddings = np.load(EMBEDDINGS_FILE)
            with open(DOCUMENTS_FILE, "r", encoding="utf-8") as f:
                self.documents = [json.loads(line)["text"] for line in f]
        else:
            print("[INFO] No cache found. Computing embeddings...")
            self.documents = load_documents()
            self.embeddings = embed_documents(self.documents, model_name)
            os.makedirs(CACHE_DIR, exist_ok=True)
            np.save(EMBEDDINGS_FILE, self.embeddings)
            with open(DOCUMENTS_FILE, "w", encoding="utf-8") as f:
                for doc in self.documents:
                    f.write(json.dumps({"text": doc}, ensure_ascii=False) + "\n")
            print("[INFO] Embeddings cached to disk (.npy + .jsonl).")

        dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(np.array(self.embeddings))

    def retrieve(self, query, top_k=1):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_embedding), top_k)
        return [self.documents[idx] for idx in indices[0]]

if __name__ == "__main__":
    retriever = Retriever()
    query = input("Enter your query you beautiful human being: ")
    result = retriever.retrieve(query, top_k=1)
    print("\nTop result:")
    print(result[0])