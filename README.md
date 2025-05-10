# Conversational AI Study Assistant

Welcome to my **Conversational AI Study Assistant** project!

This is a lightweight yet powerful educational tool designed to assist students and AI enthusiasts in learning and exploring foundational and advanced topics in **Artificial Intelligence** using a **Retrieval-Augmented Generation (RAG)** approach 😊

---

## Features:

* **Knowledge Augmented Generation**: Uses a custom RAG pipeline that retrieves top documents before generating answers.
* **Smart Retrieval**: FAISS-based document search over a curated set of AI knowledge bases (Wikipedia, ArXiv abstracts, intro notes).
* **LLM-Powered Generation**: Uses local models (e.g., via `llama3` through Ollama or similar).
* **CodeCarbon Integration**: Tracks CO₂ emissions and energy usage for each query.
* **Evaluation Suite**: Benchmarks QA performance and logs accuracy & latency.
* **Streamlit Interface**: Clean, themed, and interactive UI with Chibi Alan Turing for fun :D

---

## Project Structure

```txt
.
├── data/                  # Knowledge base (.txt scraped from wiki, arxiv, etc.)
├── cached/                # Cached document embeddings (ignored by git)
├── logs/                  # GUI and evaluation logs (ignored by git)
├── scripts/               # Utilities like wiki/arxiv scrapers
├── src/                   # Core logic: retrieval, embeddings, generation, evaluation
├── app.py                 # Streamlit GUI entry point
├── main.py                # Command-line entry for raw RAG interaction
├── rag_pipeline.py        # Core RAG pipeline: retrieval + generation
├── requirements.txt       # Required Python packages
└── README.md              # This file
```

---

## Installation

1. **Clone the repo**:

```bash
git clone https://github.com/AsmaGhamacha/Conversational_Ai.git
cd Conversational_Ai
```

2. **Create and activate a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

---

## Data Preparation

Scrape Wikipedia or ArXiv papers to populate the knowledge base:

```bash
python scripts/wiki_scraper.py
python scripts/download_arxiv_papers.py
```

Embeddings and index are automatically created when running the app for the first time.

---

## Evaluation

To evaluate the agent's performance:

```bash
python src/evaluation.py
```

This uses the file `data/eval_questions.jsonl` and logs:

* Accuracy (%)
* Average Latency (s)
* Per-query results to `logs/eval_log.csv`

---

## Example CLI Usage

```bash
python main.py
# Enter your question:
> What is reinforcement learning?
```
![image](https://github.com/user-attachments/assets/b2775d54-76b8-435b-bf4e-fb116eb147f0)

---

## Launch Streamlit App

```bash
streamlit run app.py
```

The app includes:

* Query input
* output formatting (questions and answers's history is saved)
* CO2 impact and duration per response

---

## Sample Evaluation Output

```
Accuracy: 60.0%
Average Latency: 6.91s
```

---

## 🤝 Acknowledgements
* https://huggingface.co/blog/ngxson/make-your-own-rag
* [FAISS](https://github.com/facebookresearch/faiss)
* [sentence-transformers](https://www.sbert.net/)
* [CodeCarbon](https://mlco2.github.io/codecarbon/)
* Wikipedia, ArXiv and all open-access knowledge contributors

---

## 👩‍💻 Author

Made with ❤️ by **Asma Ghamacha** for academic AI exploration.

---

## 📜 License

This project is licensed under the MIT License.
