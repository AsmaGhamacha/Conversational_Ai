# file goal: to create vector representations of text docs in data
"""
1. Import necessary libraries
2. load the data
3. using sentence-transoformers to create embeddings for the text data
4. return docs and embeddings
"""

import os
from sentence_transformers import SentenceTransformer

def load_documents():
    folders = [
        "data/wiki",
        "data/ai_arxiv"
    ]
    
    documents = []
    for folder in folders:
        for filename in os.listdir(folder):
            if filename.endswith(".txt"):
                with open(os.path.join(folder, filename), "r", encoding="utf-8") as f:
                    documents.append(f.read())
    
    print(f"[LOADED]  {len(documents)} documents from {len(folders)} folders.")
    return documents

def embed_documents(documents, model_name='thenlper/gte-small'):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(documents, show_progress_bar=True)
    return embeddings

if __name__ == "__main__":
    docs = load_documents()
    embeddings = embed_documents(docs)
    print(f"Loaded {len(docs)} documents.")
    print(f"Embeddings shape: {embeddings.shape}")