import json
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score

def main():
    with open('src/processed_data.json', 'r') as f:
        data = json.load(f)
        
    texts = [sample['text'] for sample in data]
    labels = [sample['mode'] for sample in data]
    
    print("Loading SentenceTransformer model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    print("Encoding texts...")
    embeddings = model.encode(texts, show_progress_bar=True)
    
    # Calculate Silhouette Score
    score = silhouette_score(embeddings, labels)
    print(f"Silhouette Score: {score:.4f}")
    
    # Dimensionality Reduction
    print("Performing PCA...")
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(embeddings)
    
    print("Performing t-SNE...")
    tsne = TSNE(n_components=2, random_state=42)
    tsne_result = tsne.fit_transform(embeddings)
    
    # Plotting
    os.makedirs('figures', exist_ok=True)
    os.makedirs('results', exist_ok=True)
    
    plt.figure(figsize=(16, 6))
    
    plt.subplot(1, 2, 1)
    sns.scatterplot(x=pca_result[:,0], y=pca_result[:,1], hue=labels, palette='viridis')
    plt.title('PCA of Text Embeddings by Mode')
    
    plt.subplot(1, 2, 2)
    sns.scatterplot(x=tsne_result[:,0], y=tsne_result[:,1], hue=labels, palette='viridis')
    plt.title('t-SNE of Text Embeddings by Mode')
    
    plt.savefig('figures/embedding_clusters.png')
    
    # Save results
    results = {
        "silhouette_score": float(score),
        "pca_variance_ratio": pca.explained_variance_ratio_.tolist()
    }
    with open('results/experiment2_metrics.json', 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
