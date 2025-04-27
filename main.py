# main.py

from src.retrieval import Retriever
from src.generation import Generator

def main():
    retriever = Retriever()
    generator = Generator(model_name="llama3")

    print("Hellloooo! I'm a conversation AI agent here to assist you. Type 'Bye' to exit.\n")

    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit", "bye"]:
            break

        retrieved_context = retriever.retrieve(query, top_k=1)[0]
        answer = generator.generate_answer(query, retrieved_context)

        print(f"\nAgent: {answer}\n")

if __name__ == "__main__":
    main()
