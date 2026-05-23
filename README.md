# 'Modes' in LLM Reading

## Overview
This repository contains a fully automated research project that investigates whether Large Language Models (LLMs) can detect distinct text origin 'modes' (e.g., Dictated, Typed, and AI-Generated) and if these modes can be isolated as latent variables in text embeddings. The project combines zero-shot classification and embedding-based clustering to analyze these text artifacts.

## Key Findings
- **LLM Detection Accuracy**: An LLM (`gpt-4o-mini`) achieved 63.3% accuracy in zero-shot classification of text origin.
- **Successes**: The model accurately detected 'AI-Generated' text (Recall: 1.00) and 'Typed' text with orthographic errors (Recall: 0.90).
- **Failures**: The model completely failed to zero-shot detect 'Dictated' text containing phonetic homophones, misclassifying them as either 'AI-Generated' or 'Typed'.
- **Latent Embedding Clustering**: Embeddings extracted using `all-MiniLM-L6-v2` exhibited a moderate Silhouette Score of 0.3035, confirming that 'mode' manifests as a detectable latent variable, with the primary PCA component capturing over 55% of the variance separating Clean/AI text from Error-Injected text.

## Structure
- `planning.md`: The initial hypothesis, setup, and experimental design.
- `REPORT.md`: The complete research report detailing methodology, results, and discussion.
- `src/`: Python scripts for data preparation (`data_prep.py`), classification (`experiment1.py`), and embedding clustering (`experiment2.py`).
- `results/`: Output JSON files containing predictions and computed metrics.
- `figures/`: Visualizations of the embedding clusters (PCA and t-SNE).
- `datasets/`: (Local) Raw data containing homophones, ASR errors, and AI generations.

## How to Reproduce
1. **Environment Setup**: Ensure you have Python 3.10+. This project uses `uv` for dependency management.
   ```bash
   uv pip install pandas scikit-learn matplotlib seaborn openai sentence-transformers torch
   ```
2. **Data Preparation**: Run the script to aggregate and inject errors into a unified dataset.
   ```bash
   python src/data_prep.py
   ```
3. **Run Experiments**: Make sure the `OPENAI_API_KEY` is exported.
   ```bash
   python src/experiment1.py
   python src/experiment2.py
   ```
4. **Results**: Review the output in the `results/` and `figures/` directories.

Please refer to [REPORT.md](./REPORT.md) for full details on the experimental setup and findings.