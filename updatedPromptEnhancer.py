import ollama
import json
from langchain_ollama import OllamaEmbeddings
#from langchain_community.embeddings import OllamaEmbeddings
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import os

# Load the embedding model
embedding_function = OllamaEmbeddings(model="deepseek-r1")

# LLM for prompt enrichment
chosen_model = 'hf.co/mradermacher/Llama-3.2-3B-Instruct-uncensored-GGUF'

# Path to store past prompts and embeddings
DATA_FILE = "past_prompts.json"

# Load previous prompts
def load_history():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Save updated history
def save_history(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Core LLM tasks
def extract_keyword(prompt):
    response = ollama.generate(
        model=chosen_model,
        prompt=f"Identify the product/item in {prompt}. For example, in the phrase Batman Coffee Mug, you have to identify Coffee Mug as the product/item. Respond with just the product name (like in my case, you just have to output Coffee Mug) and nothing else. A few examples of product types are as follows: 1. T-Shirts 2. Hoodies 3. Sweatshirts 4. Tank Tops 5. Crop tops 6. Crop hoodie 7. Maternity dresses 8. Caps 9. Long Sleeve Shirts 10. Polo Shirts 11. Dresses 12. Skirts 13. Leggings 14. Scarves 15. Bandanas 16. Aprons 17. Phone Cases 18. Laptop Sleeves 19. Tablet Sleeves 20. Mugs 21. Water Bottles 22. Tote Bags 23. Backpacks 24. Drawstring Bags 25. Beach Towels 26. Blankets 27. Pillows 28. Posters 29. Stickers 30. Buttons 31. Magnets 32. Keychains 33. Pin Badges 34. Pet Accessories (such as pet tags, pet bowls, and pet bandanas) 35. Home Decor (such as wall art, throw pillows, and blankets) 36. Accessories (such as hats, socks, and jewelry) 37. Stationery (such as notebooks, journals, and greeting cards) 38. Pet Beds 39. Shorts 40. Joggers "
    )
    return response.get('response', '').strip()

def extract_theme(prompt):
    response = ollama.generate(
        model=chosen_model,
        prompt=f"Identify the theme/description in {prompt}. For example, in the phrase Batman Coffee Mug, you have to identify Batman as the theme/description. Respond with just the description/theme (like in my case, you just have to output Batman) and nothing else"
    )
    return response.get('response', '').strip()

def enhance_prompt(theme):
    response = ollama.generate(
        model=chosen_model,
        prompt=f"Enhance the following prompt: {theme} to make it suitable for image generation. Only output the enhanced prompt and nothing else"
    )
    return response.get('response', '').strip()

# Semantic search against history
def semantic_search(query_embedding, history, top_k=3):
    if not history:
        return []

    embeddings = np.array([item['embedding'] for item in history]).astype(np.float32)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    distances, indices = index.search(np.array([query_embedding]), top_k)
    results = []
    for i, dist in zip(indices[0], distances[0]):
        item = history[i]
        results.append({
            "prompt": item["original_prompt"],
            "enhanced_prompt": item["enhanced_prompt"],
            "distance": float(dist)
        })
    return results

def main():
    user_input = input("Enter your prompt: ").strip()
    if not user_input:
        print("Prompt cannot be empty.")
        return

    # Extract details
    keyword = extract_keyword(user_input)
    theme = extract_theme(user_input)
    enhanced = enhance_prompt(theme)
    embedding = embedding_function.get_text_embedding(enhanced)
    #embedding = embedding_model.encode([enhanced])[0]

    # Load history and perform semantic search
    history = load_history()
    similar = semantic_search(embedding, history)

    # Append current prompt to history
    history.append({
        "original_prompt": user_input,
        "keyword": keyword,
        "theme": theme,
        "enhanced_prompt": enhanced,
        "embedding": embedding.tolist()  # Convert for JSON storage
    })
    save_history(history)

    # Output
    output = {
        "original_prompt": user_input,
        "keyword": keyword,
        "theme": theme,
        "enhanced_prompt": enhanced,
        "semantic_similar_prompts": similar
    }

    print(json.dumps(output, indent=4))


if __name__ == "__main__":
    main()
