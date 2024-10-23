# __init__.py

# Example: Importing specific functions/classes for easier access
from .scraper import scrape_courses
from .embedding_model import create_embeddings
from .search_interface import search_courses

__all__ = ['scrape_courses', 'create_embeddings', 'search_courses']
