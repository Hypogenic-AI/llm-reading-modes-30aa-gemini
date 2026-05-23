import json
import random
import re
import os

random.seed(42)

def keyboard_typo(word):
    keyboard = {
        'a': 'qwsz', 'b': 'vghn', 'c': 'xdfv', 'd': 'sfcx', 'e': 'wsdr',
        'f': 'drtgv', 'g': 'ftyhb', 'h': 'gyujn', 'i': 'ujko', 'j': 'huikm',
        'k': 'jiolm', 'l': 'kop', 'm': 'njk', 'n': 'bhjm', 'o': 'iklp',
        'p': 'ol', 'q': 'wa', 'r': 'edft', 's': 'awedxz', 't': 'rfgy',
        'u': 'yhji', 'v': 'cfgb', 'w': 'qase', 'x': 'zsdc', 'y': 'tghu',
        'z': 'asx'
    }
    if len(word) < 2: return word
    pos = random.randint(0, len(word)-1)
    char = word[pos].lower()
    if char in keyboard:
        typo_char = random.choice(keyboard[char])
        if word[pos].isupper(): typo_char = typo_char.upper()
        return word[:pos] + typo_char + word[pos+1:]
    return word

def inject_errors(text, error_dict, error_type, rate=0.15):
    words = re.findall(r'\b\w+\b', text)
    num_errors = max(1, int(len(words) * rate))
    indices_to_modify = random.sample(range(len(words)), min(num_errors, len(words)))
    
    modified_text = text
    for i in indices_to_modify:
        word = words[i]
        if error_type == "homophone":
            if word.lower() in error_dict:
                modified_text = re.sub(rf'\b{word}\b', error_dict[word.lower()], modified_text, count=1)
        elif error_type == "typo":
            typo_word = keyboard_typo(word)
            modified_text = re.sub(rf'\b{word}\b', typo_word, modified_text, count=1)
    return modified_text

def main():
    try:
        with open('datasets/guychuk_typos-misspellings-homophones-dataset/samples.json', 'r') as f:
            typo_data = json.load(f)
        homophones = {item['correct'].lower(): item['variant'].lower() for item in typo_data if item.get('type') == 'homophone'}
        for item in typo_data:
            if item.get('type') == 'homophone':
                homophones[item['variant'].lower()] = item['correct'].lower()
    except Exception as e:
        print(f"Failed to load homophones: {e}")
        homophones = {"there": "their", "their": "they're", "they're": "there", "to": "too", "too": "two", "two": "to", "accept": "except", "except": "accept"}

    # Add some common ones just in case
    homophones.update({"its": "it's", "it's": "its", "your": "you're", "you're": "your", "then": "than", "than": "then"})

    with open('datasets/jjz5463_llm-detection/samples.json', 'r') as f:
        llm_data = json.load(f)

    dataset = []
    for idx, item in enumerate(llm_data[:50]):
        prompt = item.get('prompts', '')
        ai_text = item.get('generations by the LLM.', '')
        
        if '# ' in prompt:
            parts = prompt.split('# ')
            if len(parts) > 1:
                source_text = parts[1].split('\n\n')[1] if len(parts[1].split('\n\n')) > 1 else parts[1][:500]
            else:
                source_text = prompt[:500]
        else:
            source_text = prompt[:500]
            
        if len(source_text.split()) < 10:
            continue
            
        dataset.append({
            "id": idx,
            "mode": "AI_Generated",
            "text": ai_text[:1000]
        })
        
        dictated_text = inject_errors(source_text, homophones, "homophone", rate=0.2)
        dataset.append({
            "id": idx,
            "mode": "Dictated",
            "text": dictated_text[:1000]
        })
        
        typed_text = inject_errors(source_text, homophones, "typo", rate=0.1)
        dataset.append({
            "id": idx,
            "mode": "Typed",
            "text": typed_text[:1000]
        })

    os.makedirs('src', exist_ok=True)
    with open('src/processed_data.json', 'w') as f:
        json.dump(dataset, f, indent=2)
    print(f"Generated {len(dataset)} samples.")

if __name__ == "__main__":
    main()
