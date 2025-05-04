# scripts/wiki_scraper.py

import os
import wikipediaapi

output_dir = "data/wiki"
os.makedirs(output_dir, exist_ok=True)

wiki = wikipediaapi.Wikipedia(
    language="en",
    user_agent="https://github.com/AsmaGhamacha/Conversational_Ai.git"
)
#List of AI topics to scrape
topics = [
    "Artificial intelligence",
    "Machine learning",
    "Deep learning",
    "Neural network",
    "Natural language processing",
    "Reinforcement learning",
    "Supervised learning",
    "Unsupervised learning",
    "Transfer learning",
    "Computer vision",
    "Speech recognition",
    "Generative adversarial network",
    "Transformer (machine learning model)",
    "Attention mechanism",
    "BERT (language model)",
    "GPT (language model)",
    "LLaMA (language model)",
    "Tokenization (NLP)",
    "Word embedding",
    "Loss function",
    "Gradient descent",
    "Backpropagation",
    "Overfitting",
    "Regularization (machine learning)",
    "Bias–variance tradeoff",
    "Activation function",
    "Dropout (neural networks)",
    "Convolutional neural network",
    "Recurrent neural network",
    "Long short-term memory",
    "Self-supervised learning",
    "Zero-shot learning",
    "Few-shot learning",
    "Prompt engineering",
    "Text classification",
    "Language model",
    "Explainable artificial intelligence",
    "Ethics of artificial intelligence",
    "Turing test",
    "AI alignment",
    "Transformer (machine learning model)",
    "Reinforcement learning",
    "Neural network",
    "Gradient descent",
    "Overfitting",
    "Loss function",
    "Transfer learning",
    "Activation function",
    "Supervised learning",
    "Convolutional neural network"
]

for topic in topics:
    page = wiki.page(topic)

    if not page.exists():
        print(f"[SKIP] '{topic}' not found.")
        continue

    content = page.summary + "\n\n"

    for section in page.sections:
        content += f"\n## {section.title}\n{section.text}\n"

    filename = topic.lower().replace(" ", "_").replace("/", "_") + ".txt"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())

    print(f"[SAVED] {filename}")
