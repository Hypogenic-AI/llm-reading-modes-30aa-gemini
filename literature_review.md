# Literature Review: 'Modes' in LLM Reading

## Research Area Overview
Large Language Models (LLMs) are increasingly used for forensic linguistics, authorship attribution, and text source characterization. This research explores whether LLMs can detect 'modes'—latent variables such as whether text was dictated, written by another LLM, or influenced by hardware (e.g., keyboard layout). Current literature confirms that LLMs have distinct writing signatures and that text source artifacts (like ASR errors) are systematic and detectable.

## Key Papers

### 1. Authorship Attribution in the Era of LLMs: Problems, Methodologies, and Challenges (2024)
- **Authors**: Baixiang Huang, Canyu Chen, Kai Shu
- **Key Contribution**: A comprehensive survey of how LLMs are used for authorship attribution and the challenges posed by LLM-generated text.
- **Relevance**: Provides the foundation for understanding how "mode" (as authorship) is currently handled.

### 2. FAID: Fine-grained AI-generated Text Detection (2025)
- **Authors**: Ta et al.
- **Key Contribution**: Introduces multi-task auxiliary and multi-level contrastive learning for fine-grained detection (Human vs LLM vs Human-LLM collaboration).
- **Dataset**: FAIDSet.
- **Relevance**: Directly addresses the "multi-mode" nature of modern text generation.

### 3. Neural Authorship Attribution: Stylometric Analysis on Large Language Models (2023)
- **Authors**: Kumarage et al.
- **Key Contribution**: Scrutinizes variations in LLM writing signatures using stylometric analysis.
- **Relevance**: Confirms that LLMs have detectable latent styles.

### 4. Lost in Transcription: How Speech-to-Text Errors Derail Code Understanding (2026)
- **Authors**: Havare et al.
- **Key Contribution**: Systematically characterizes ASR errors and their impact.
- **Relevance**: Provides evidence for "dictated mode" artifacts.

### 5. Language as a Latent Variable for Reasoning Optimization (2026)
- **Authors**: Wu et al.
- **Key Contribution**: Explores language as a latent variable that modulates model internal pathways.
- **Relevance**: High theoretical relevance for "isolating mode as a latent variable."

## Common Methodologies
- **Contrastive Learning**: Used to distinguish between closely related text sources (e.g., different LLMs or Human-LLM co-writing).
- **Stylometric Analysis**: Using traditional and neural features (punctuation, syntax, vocabulary) to identify signatures.
- **Error Pattern Analysis**: Specifically for ASR/OCR, looking at phonetic vs. orthographic mistake distributions.

## Standard Baselines
- **RoBERTa-based Detectors**: Common for binary AI vs. Human classification.
- **PPL (Perplexity) based methods**: Detecting AI text via low entropy.
- **Stylometric Classifiers**: Traditional SVMs with linguistic features.

## Datasets in the Literature
- **FAIDSet**: Multi-source AI/Human text.
- **MixSet**: Collaborative writing.
- **ASDF**: ASR differential testing data.
- **Wiki-Typo**: Keyboard/typing mistakes.

## Gaps and Opportunities
- **Isolation of Hardware Modes**: Limited research on detecting keyboard layout influence (e.g., QWERTY vs. Dvorak vs. AZERTY) purely from text artifacts.
- **Latent Variable Interpretability**: While models can detect modes, isolating them as interpretable latent variables for downstream control is still nascent.

## Recommendations for Our Experiment
- **Recommended datasets**: `guychuk/typos-misspellings-homophones-dataset` for keyboard vs phonetic modes; `jjz5463/llm-detection-generation-1.0` for LLM modes.
- **Recommended baselines**: Contrastive learning models (like FAID) and stylometric feature extractors.
- **Recommended metrics**: PER (Phonetic Error Rate) vs. WER (Word Error Rate) to distinguish dictation from typing.
