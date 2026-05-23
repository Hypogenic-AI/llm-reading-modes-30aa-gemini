## Motivation & Novelty Assessment

### Why This Research Matters
Large Language Models interpret text from various sources, each carrying distinct artifacts (modes) such as phonetic errors from dictation, typographical errors from keyboard layouts, or stylistic signatures from other LLMs. Understanding and detecting these modes can vastly improve authorship attribution, forensic linguistics, and context-aware error correction.

### Gap in Existing Work
Current research primarily focuses on binary classification (AI vs. Human) or specific isolated detection (e.g., ASR error correction). While stylometric analysis and contrastive learning are used for fine-grained detection (e.g., Human-LLM collaboration), there is limited research on treating the origin "mode" (Dictated, Typed, AI-Generated) as a unified, interpretable latent variable that can be robustly identified across diverse text types.

### Our Novel Contribution
This research tests the hypothesis that "mode" can be isolated as a latent variable by combining diverse artifact datasets (keyboard typos, ASR phonetic errors, and LLM text). We will evaluate whether LLMs can explicitly zero-shot identify these modes and whether standard text embeddings inherently cluster these modes in their latent space.

### Experiment Justification
- Experiment 1 (Zero-Shot Mode Detection): Evaluates if state-of-the-art LLMs possess the emergent ability to detect dictation vs. typing vs. AI modes based on text artifacts.
- Experiment 2 (Latent Embedding Analysis): Investigates whether "mode" is already captured as a separable latent variable in standard text embedding spaces (e.g., using clustering metrics on OpenAI/HuggingFace embeddings).

## Research Question
What specific text generation 'modes' (e.g., dictated, typed, AI-generated) can LLMs detect, and can we isolate 'mode' as a structured latent variable in the interpretation of text?

## Background and Motivation
See Motivation & Novelty Assessment above.

## Hypothesis Decomposition
1. **Detectability**: LLMs can accurately classify text into Dictated, Typed, and AI-Generated modes based on inherent artifacts.
2. **Latent Representation**: Standard text embeddings naturally cluster texts by these modes, proving that "mode" is a captured latent variable.

## Proposed Methodology

### Approach
We will construct a composite dataset combining samples from existing typo/spelling correction datasets, ASR error datasets, and LLM detection datasets. We will then perform both prompt-based classification using an LLM API and embedding-based clustering analysis.

### Experimental Steps
1. **Data Preparation**: Unify samples from `guychuk/typos-misspellings-homophones-dataset` (Typed mode), `youngwoo3283_asr_spellingCorrection_24k` (Dictated mode), and `jjz5463/llm-detection` (AI mode).
2. **Experiment 1 (LLM API Evaluation)**: Prompt a SOTA LLM (e.g., GPT-4o or Claude via API) to classify the mode of each sample. Record accuracy, precision, and recall.
3. **Experiment 2 (Embedding Analysis)**: Extract sentence embeddings for all samples using a model like `all-MiniLM-L6-v2` or OpenAI embeddings. Use PCA/t-SNE for visualization and Silhouette Score to measure the separation of modes.

### Baselines
- Random classification (for LLM API evaluation).
- Traditional stylometric feature baseline (if needed, though embedding comparison serves as a strong baseline for latent representation).

### Evaluation Metrics
- Classification Metrics: Accuracy, Precision, Recall, F1-score for each mode.
- Clustering Metrics: Silhouette Score, Calinski-Harabasz Index for embedding separation.

### Statistical Analysis Plan
- Calculate mean performance and 95% confidence intervals for classification metrics.
- Perform ANOVA to determine if Silhouette scores for mode clusters are statistically significant compared to random groupings.

## Expected Outcomes
We expect LLMs to achieve significantly better-than-random accuracy in detecting the modes, and we expect embeddings to show distinct clusters, validating that mode is a detectable latent variable.

## Timeline and Milestones
- Phase 2 (Environment Setup): 10 mins.
- Phase 3 (Implementation of data prep and experiment harness): 30 mins.
- Phase 4 (Experimentation): 30 mins.
- Phase 5 (Analysis & Plotting): 20 mins.
- Phase 6 (Documentation): 20 mins.

## Potential Challenges
- Small sample size per dataset may limit statistical power; we will rely on the provided 50-100 sample subsets but consider it a proof-of-concept.
- Difficulty in isolating "mode" from topic or content; we will use embedding techniques like PCA to identify the specific principal components that correlate with mode rather than content.

## Success Criteria
- Successful execution of both prompt-based and embedding-based experiments.
- Clear statistical evidence supporting or refuting the hypothesis.
- Generation of a comprehensive `REPORT.md` detailing the findings.