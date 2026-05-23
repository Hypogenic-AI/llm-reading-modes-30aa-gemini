# Resources Catalog

### Summary
This document catalogs all resources gathered for the research into 'Modes' in LLM Reading. Resources include key research papers, datasets for various modes (AI-generated, dictation, typing errors), and code repositories for detection and authorship analysis.

### Papers
Total papers downloaded: 8

| Title | Authors | Year | File | Key Info |
|-------|---------|------|------|----------|
| Authorship Attribution in LLMs | Huang et al. | 2024 | papers/2406_authorship_attribution_llm.pdf | Survey of LLM AA. |
| AI-generated Text Forensics | (Survey) | 2024 | papers/2403_ai_generated_text_forensics.pdf | Survey of forensics. |
| FAID: Fine-grained Detection | Ta et al. | 2025 | papers/2410_faid_fine_grained_detection.pdf | Human-LLM collab detection. |
| Neural Authorship Attribution | Kumarage et al. | 2023 | papers/2307_neural_authorship_attribution.pdf | Stylometrics for LLMs. |
| Language as a Latent Variable | Wu et al. | 2026 | papers/2601_language_latent_variable.pdf | Theory of latent modes. |
| Lost in Transcription (ASR) | Havare et al. | 2026 | papers/2601_lost_in_transcription_asr.pdf | Dictation artifacts. |
| ASR Error Correction | (BART) | 2022 | papers/2202_asr_error_correction_bart.pdf | Error modeling for ASR. |
| ASDF: ASR Testing | (ASDF) | 2023 | papers/2302_asdf_asr_testing.pdf | Phonetic error alignment. |

### Datasets
Total datasets downloaded (sampled): 3

| Name | Source | Size | Task | Location | Notes |
|------|--------|------|------|----------|-------|
| Typos/Misspellings/Homophones | guychuk (HF) | 100 samples | Mode Detection | datasets/guychuk_typos... | Good for Keyboard vs Phonetic modes. |
| ASR Spelling Correction | youngwoo (HF) | 100 samples | ASR Correction | datasets/youngwoo3283_asr... | Specific to ASR artifacts. |
| LLM Detection | jjz5463 (HF) | 50 samples | AI detection | datasets/jjz5463_llm-detection | Baseline AI detection. |

### Code Repositories
Total repositories cloned: 7

| Name | URL | Purpose | Location | Notes |
|------|-----|---------|----------|-------|
| FAID | github.com/mbzuai-nlp/FAID | Fine-grained detection | code/FAID | Core implementation of FAID. |
| LLMauthorbench | github.com/LLMauthorbench/... | Authorship Bench | code/LLMauthorbench | Authorship attribution tools. |
| CollabStory | github.com/saranya-v/... | Human-AI Collab | code/CollabStory | Collaborative writing analysis. |
| MixSet | github.com/Dongping-Chen/... | MixSet Dataset/Code | code/MixSet | MixSet implementation. |
| MarkLLM | github.com/THU-BPM/MarkLLM | Watermarking | code/MarkLLM | Watermarking tools. |
| HumanAI_Auth | github.com/AARichburg/... | Authorship Analysis | code/HumanAI_Auth | Benchmarking. |
| AuthAttr_zge | github.com/zge/... | Stylometric model | code/AuthAttr_zge | Neural authorship attribution. |

### Recommendations for Experiment Design

1.  **Primary dataset(s)**: Use the `guychuk/typos-misspellings-homophones-dataset` to contrast orthographic (keyboard-like) mistakes with phonetic (dictation-like) mistakes.
2.  **Baseline methods**: Use RoBERTa-large with contrastive loss (as in FAID) to see if these modes cluster naturally in latent space.
3.  **Evaluation metrics**: Measure the isolation of the "mode" variable using Disentanglement Metrics (e.g., MIG, FactorVAE score) if a generative model is used, or classification accuracy if labels are available.
4.  **Code to adapt/reuse**: The FAID repository provides a strong foundation for multi-task and contrastive learning which is ideal for isolating latent modes.
