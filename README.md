# MovieLens Recommendation System

This project is a movie recommendation system built using collaborative filtering on the MovieLens 10M dataset. It supports both:

- **User-based recommendations** using SVD (Singular Value Decomposition)
- **Item-based recommendations** using KNN (K-Nearest Neighbors)

The project includes:
- Model training scripts (`train.py`, `item_knn.py`)
- Recommendation functions (`recommend.py`, `item_recom.py`)
- A FastAPI web interface with endpoints for recommending movies by user or by similar items
- Unit tests and project structure following best practices

Tools used: Python, Surprise, FastAPI, Pytest, Git

