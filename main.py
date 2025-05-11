# main.py

from src.retrieval import Retriever
from src.generation import Generator
import time
import csv
import os
from datetime import datetime

LOG_FILE = "logs/conversation_log.csv"

def log_latency(query, latency):
    os.makedirs("logs", exist_ok=True)
    write_header = not os.path.exists(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        if write_header:
            writer.writerow(["Timestamp", "Query", "Response Time (s)"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), query, round(latency, 2)])


def main():
    retriever = Retriever()
    generator = Generator()

    print("Hellloooo! I'm a conversation AI agent here to assist you. Type 'Bye' to exit.\n")

    while True: 
        query = input("You: ")
        if query.lower() in ["exit", "quit", "bye"]:
            break

        start_time = time.time()

        retrieved_context = retriever.retrieve(query, top_k=1)[0]
        answer = generator.generate_answer(query, retrieved_context)

        end_time = time.time()
        latency = end_time - start_time

        print(f"\nAgent: {answer}\n")
        print(f"Response time: {latency:.2f} seconds\n")

        log_latency(query, latency)

if __name__ == "__main__":
    main()