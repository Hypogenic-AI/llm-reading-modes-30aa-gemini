import json
import os
import time
from openai import OpenAI
from sklearn.metrics import classification_report, accuracy_score

def classify_text(client, text):
    prompt = f"""You are an expert forensic linguist. Analyze the following text and determine its origin 'mode'.
The text could be:
1. 'AI_Generated': Produced by a Large Language Model (look for typical AI style, structure, or lack of human errors).
2. 'Dictated': Contains phonetic errors or homophone substitutions (e.g., 'there' instead of 'their', 'accept' instead of 'except') typical of speech-to-text / dictation.
3. 'Typed': Contains orthographic or keyboard typos (e.g., adjacent key presses, transposed letters).

Text: "{text}"

Output ONLY the exact mode name: 'AI_Generated', 'Dictated', or 'Typed'. No other text."""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=10
        )
        prediction = response.choices[0].message.content.strip()
        
        # Clean up prediction
        for mode in ['AI_Generated', 'Dictated', 'Typed']:
            if mode.lower() in prediction.lower():
                return mode
        return "Unknown"
    except Exception as e:
        print(f"API Error: {e}")
        return "Error"

def main():
    with open('src/processed_data.json', 'r') as f:
        data = json.load(f)
    
    client = OpenAI() # expects OPENAI_API_KEY in env
    
    results = []
    y_true = []
    y_pred = []
    
    print(f"Starting classification for {len(data)} samples...")
    for idx, sample in enumerate(data):
        pred = classify_text(client, sample['text'])
        
        results.append({
            "id": sample['id'],
            "true_mode": sample['mode'],
            "predicted_mode": pred,
            "text": sample['text']
        })
        y_true.append(sample['mode'])
        y_pred.append(pred)
        
        if (idx + 1) % 10 == 0:
            print(f"Processed {idx + 1}/{len(data)}")
            
    # Evaluation
    valid_indices = [i for i, p in enumerate(y_pred) if p in ['AI_Generated', 'Dictated', 'Typed']]
    y_true_valid = [y_true[i] for i in valid_indices]
    y_pred_valid = [y_pred[i] for i in valid_indices]
    
    acc = accuracy_score(y_true_valid, y_pred_valid)
    report = classification_report(y_true_valid, y_pred_valid, output_dict=True, zero_division=0)
    
    print(f"Accuracy: {acc:.4f}")
    
    os.makedirs('results', exist_ok=True)
    with open('results/experiment1_predictions.json', 'w') as f:
        json.dump(results, f, indent=2)
        
    with open('results/experiment1_metrics.json', 'w') as f:
        json.dump({"accuracy": acc, "report": report}, f, indent=2)
        
if __name__ == "__main__":
    main()
