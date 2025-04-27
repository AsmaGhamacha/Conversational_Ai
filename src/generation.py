#file goal: full RAG basically
"""
1. retrieving best doc
2. building prompt
3. send the prompt to llama3
4. receiving the answer
"""
import requests

class Generator:
    def __init__(self, model_name="llama3"):
        """generator"""
        self.model = model_name
        self.url = "http://localhost:11434/api/generate"

    def generate_answer(self, query, context):
        prompt = f"""You are an AI assistant. Use the following context to answer the user's question.

Context: {context}

User Question: {query}

Answer:"""

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.url, json=payload)
        
        if response.status_code == 200:
            return response.json()["response"].strip()
        else:
            raise Exception(f"Failed to generate response: {response.text}")

if __name__ == "__main__":
    gen = Generator()
    context = "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines..."
    query = input("Enter your question: ")
    answer = gen.generate_answer(query, context)
    print("\nGenerated Answer:")
    print(answer)