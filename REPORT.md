# Research Report: 'Modes' in LLM Reading - Isolating Latent Variables in Text

## 1. Executive Summary
This research investigates whether Large Language Models (LLMs) can detect distinct origin 'modes' of text (e.g., Dictated, Typed, and AI-Generated) and if these modes can be isolated as latent variables in text embeddings. Through a combination of zero-shot classification via a state-of-the-art LLM and embedding-based cluster analysis, we found that LLMs possess moderate capability (63.3% accuracy) to zero-shot classify text origins, primarily succeeding with 'AI-Generated' and 'Typed' text but failing to isolate 'Dictated' text containing phonetic homophones. Furthermore, text embeddings exhibited a moderate degree of clustering by mode (Silhouette Score: 0.3035), suggesting that 'mode' does exist as a detectable latent variable, though distinguishing certain modes (like dictation) requires further fine-tuning.

## 2. Research Question & Motivation
**Hypothesis Tested:** Large language models (LLMs) can detect various 'modes' in text (dictated, typed, AI-generated), and 'mode' can be isolated as a structured latent variable in the interpretation of text.

**Motivation:** As text generation pipelines become multimodal—blending human typing, speech-to-text dictation, and AI generation—understanding the artifacts left behind is critical for authorship attribution, forensic linguistics, and context-aware error correction. While existing work focuses heavily on binary "Human vs. AI" detection or specific ASR error correction, this research seeks to generalize these artifacts into an interpretable "mode" latent variable.

## 3. Methodology
### Datasets and Preparation
We utilized a combination of resources from the pre-gathered workspace:
- **jjz5463_llm-detection**: Provided baseline AI-generated text and human prompts.
- **guychuk_typos-misspellings-homophones-dataset**: Provided phonetic errors (homophones) to simulate "Dictated" text and orthographic keyboard typos to simulate "Typed" text.

To avoid language and length confounds, we generated a balanced composite dataset (150 samples) using a common set of English source texts. 
- **AI_Generated**: Used the direct LLM generation from the `jjz5463` dataset.
- **Dictated**: Source text was injected with phonetic/homophone errors (e.g., 'there' for 'their').
- **Typed**: Source text was injected with keyboard proximity typos using a synthetic typo generator.

### Experimental Setup
**Experiment 1: Zero-Shot Classification**
- **Model**: OpenAI `gpt-4o-mini` API (Temperature: 0).
- **Prompt**: Asked the LLM to zero-shot classify texts into 'AI_Generated', 'Dictated', or 'Typed' acting as a forensic linguist.
- **Metrics**: Accuracy, Precision, Recall, F1-Score.

**Experiment 2: Latent Embedding Analysis**
- **Model**: `all-MiniLM-L6-v2` via `SentenceTransformers`.
- **Method**: Extracted embeddings for all 150 texts and analyzed latent separation using Principal Component Analysis (PCA) and t-SNE.
- **Metrics**: Silhouette Score, PCA Explained Variance.

## 4. Results

### Classification Metrics (Experiment 1)
Overall Accuracy: **63.3%**

| Mode | Precision | Recall | F1-Score | Support |
|------|-----------|--------|----------|---------|
| **AI_Generated** | 0.65 | 1.00 | 0.79 | 50 |
| **Dictated** | 0.00 | 0.00 | 0.00 | 50 |
| **Typed** | 0.65 | 0.90 | 0.76 | 50 |

*Note: The model misclassified the 50 'Dictated' samples as either 'AI_Generated' (26 samples) or 'Typed' (24 samples).*

### Embedding Clustering (Experiment 2)
- **Silhouette Score**: 0.3035 (indicating moderate cluster separation).
- **PCA Variance Ratio**: Component 1 explains 55.7% of the variance, Component 2 explains 5.1%.
- Visualizations were successfully generated using PCA and t-SNE (see `figures/embedding_clusters.png`), showing distinct boundaries primarily separating AI-generated text from the error-injected texts, though 'Typed' and 'Dictated' modes showed overlapping latent regions.

## 5. Analysis & Discussion
The results provide nuanced support for the hypothesis. 
1. **Detectability**: LLMs can zero-shot detect AI-generated and Typed modes with reasonable precision (65%) and high recall (90-100%). However, the complete failure to detect the 'Dictated' mode implies that homophone substitutions are often corrected or glossed over by the LLM in zero-shot contexts, or they are confused with simple typing errors. 
2. **Latent Representation**: A silhouette score of 0.3035 across the embeddings confirms that "mode" manifests as a latent variable. Over 55% of the variance in PCA is captured by the first component, which likely corresponds to the "Clean/AI vs. Error-Injected" axis.
3. **Synthesis**: While "mode" is a latent variable, the granularity required to separate phonetic dictation errors from orthographic typing errors zero-shot is difficult for current LLMs without fine-tuning or few-shot examples.

## 6. Limitations
- **Synthetic Error Injection**: Relying on programmatic error injection for the 'Dictated' and 'Typed' modes, rather than organic datasets (due to language differences in the provided ASR dataset), might produce artifacts that differ slightly from real-world data.
- **Model Choice**: The use of `gpt-4o-mini` instead of a larger model like `gpt-4.1` may have bottlenecked the zero-shot reasoning capabilities for detecting subtle homophone dictation errors.
- **Sample Size**: 150 samples limit the statistical power of the conclusions, acting more as a proof-of-concept.

## 7. Conclusions & Next Steps
We conclude that 'mode' acts as an identifiable latent variable in text interpretation, though current LLMs struggle to zero-shot distinguish fine-grained phonetic dictation errors from keyboard typos. The clear separation of AI-generated text from human-typed error text validates the potential of latent mode isolation.
**Next Steps**: Future research should leverage full organic ASR English datasets, utilize few-shot prompting to explicitly demonstrate phonetic versus orthographic differences, and investigate disentanglement metrics (like FactorVAE) to isolate the exact embedding dimensions responsible for "mode".