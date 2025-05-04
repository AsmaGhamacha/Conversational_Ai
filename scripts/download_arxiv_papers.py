import os
from datasets import load_dataset


dataset = load_dataset("jamescalam/ai-arxiv", split="train")

output_dir = "data/ai_arxiv"
os.makedirs(output_dir, exist_ok=True)

max_docs = 100
count = 0

#categories we care about
ai_categories = {"cs.AI", "cs.CL", "cs.LG", "stat.ML"}

for paper in dataset:
    categories = paper.get("categories", [])
    if not any(cat in ai_categories for cat in categories):
        continue

    title = paper.get("title", "").strip()
    abstract = paper.get("summary", "").strip()
    source = paper.get("source", "").strip()

    if not title or not abstract:
        continue

    #content preparation
    content = f"Title: {title}\n\nAbstract:\n{abstract}\n\nSource: {source}"
    filename = f"arxiv_{count:03}.txt"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[SAVED] : {filename}")
    count += 1
    if count >= max_docs:
        break

print(f"\n Yayyy you nail it! : {count} files saved to data/ai_arxiv/")
