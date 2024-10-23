from sentence_transformers import SentenceTransformer
import numpy as np
import json
import pickle

def create_embeddings():
    
    save_path = 'C:/Users/mt166/Ishu_Proj/analytics_vidhya_search/data/courses.json'
    # Load course data
    with open(save_path, 'r') as f:
        courses = json.load(f)

    # Load the pre-trained model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Extract course descriptions and titles for embedding
    descriptions = [course['description'] for course in courses]
    
    # Generate embeddings
    embeddings = model.encode(descriptions)

    # Save embeddings and course metadata
    path = r"C:\Users\mt166\Ishu_Proj\analytics_vidhya_search\model\embedding_model.pkl"

    
    with open(path, 'wb') as f:
        pickle.dump((embeddings, courses), f)

if __name__ == "__main__":
    create_embeddings()
