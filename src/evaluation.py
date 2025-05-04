import sys
import os
import json
import time
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from rag_pipeline import rag_respond

EVAL_PATH = "data/eval_questions.jsonl"
LOG_PATH = "logs/eval_log.csv"

def evaluate_agent():
    with open(EVAL_PATH, "r", encoding="utf-8") as f:
        eval_set = [json.loads(line) for line in f]

    total = len(eval_set)
    correct = 0
    latencies = []

    # Prepare CSV logging
    os.makedirs("logs", exist_ok=True)
    with open(LOG_PATH, "w", encoding="utf-8") as log_file:
        log_file.write("Timestamp,Query,Correct,Response Time (s)\n")

        # Loop over test queries
        for sample in eval_set:
            query = sample["query"]
            expected_keywords = sample.get("expected_keywords", [])

            start_time = time.time()
            response = rag_respond(query, k=3)
            end_time = time.time()

            response_time = round(end_time - start_time, 2)
            latencies.append(response_time)

            # Safety check + scoring
            response = response or "[No response]"
            match = all(kw.lower() in response.lower() for kw in expected_keywords)
            correct += int(match)

            # Log the result
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            safe_query = query.replace('"', '""')  # Escape quotes for CSV
            log_file.write(f'{timestamp},"{safe_query}",{match},{response_time}\n')

            print(f"\n Q: {query}")
            print(f"Match: {match}")
            print(f"Answer: {response}")
            print(f" Time: {response_time}s")

    # Final summary
    accuracy = round(correct / total * 100, 2)
    avg_latency = round(sum(latencies) / total, 2)
    print(f"\n Accuracy: {accuracy}%")
    print(f"Avg Response Time: {avg_latency}s")

if __name__ == "__main__":
    evaluate_agent()
