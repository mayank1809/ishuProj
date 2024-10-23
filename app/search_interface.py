import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

def load_model():
    # Load embeddings and course data from the saved file
    path = r"C:\Users\mt166\Ishu_Proj\analytics_vidhya_search\model\embedding_model.pkl"

    with open(path, 'rb') as f:
        embeddings, courses = pickle.load(f)
    return embeddings, courses

def search_courses(query):
    # Load the model and embeddings
    embeddings, courses = load_model()
    
    # Load the pre-trained model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Encode the user's query into an embedding
    query_embedding = model.encode([query])
    
    # Compute cosine similarity between query embedding and course embeddings
    similarities = np.dot(embeddings, query_embedding.T).squeeze()
    
    # Get top 5 most relevant courses
    top_indices = similarities.argsort()[-5:][::-1]
    
    # Return the most relevant courses
    results = [courses[i] for i in top_indices]
    return results
