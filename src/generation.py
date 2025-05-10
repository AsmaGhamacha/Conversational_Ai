#file goal: full RAG basically
"""
1. retrieving best doc
2. building prompt
3. send the prompt to llama3
4. receiving the answer
"""
import streamlit as st
import os
import requests

class Generator:
    def __init__(self, model_name="meta-llama/Meta-Llama-3-8B-Instruct"):
        """Generator using Together.ai"""
        self.model = model_name
        self.api_key = st.secrets["TOGETHER_API_KEY"]


        if not self.api_key:
            raise ValueError("TOGETHER_API_KEY not set in environment variables.")

        self.url = "https://api.together.xyz/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def generate_answer(self, query, context):
        prompt = f"""You are an AI assistant. Use the following context to answer the user's question.

Context: {context}

User Question: {query}

Answer:"""

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are an AI assistant."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 512
        }

        response = requests.post(self.url, headers=self.headers, json=payload)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        else:
            raise Exception(f"Failed to generate response: {response.text}")

if __name__ == "__main__":
    gen = Generator()
    context = "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines..."
    query = input("Enter your question: ")
    answer = gen.generate_answer(query, context)
    print("\nGenerated Answer:")
    print(answer)