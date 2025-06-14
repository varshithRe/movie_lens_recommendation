# 🎬 MovieLens Recommendation System

This project is a movie recommendation system using collaborative filtering on the MovieLens dataset. It supports both user-based and item-based recommendations and provides a FastAPI-based web service.

---

## 📁 Project Structure

.
├── app/
│ └── main.py # FastAPI app with endpoints
│
├── data/ # Raw MovieLens data (ratings.dat, movies.dat)
│
├── models/
│ ├── best_svd_model.pkl # Trained SVD model (user-based)
│ └── item_knn_tuned.pkl # Trained KNN model (item-based)
│
├── notebooks/ # For EDA or prototyping (optional)
│
├── src/
│ ├── train.py # Trains SVD model with grid search
│ ├── recommend.py # Defines get_top_n (user-based recs)
│ ├── item_knn.py # Trains item-based KNN model
│ ├── item_recom.py # Defines get_similar_movies
│ ├── svd_performance.py # Evaluates SVD model
│ ├── knn_performance.py # Evaluates KNN model
│
├── tests/
│ ├── test_endpoints.py # FastAPI endpoint tests
│ ├── test_recommend.py # Tests for get_top_n
│ ├── test_item_recom.py # Tests for get_similar_movies
│
├── .gitignore
├── Dockerfile
├── requirements.txt
├── runtime.txt
├── README.md

yaml
Copy
Edit

---

## 🚀 Features

- **User-based recommendations** (SVD)
- **Item-based recommendations** (KNN)
- **FastAPI endpoints** for both recommendation types
- **Model evaluation scripts**
- **Pytest-based test suite**

---

## 🔧 Getting Started

### Install dependencies

```bash
pip install -r requirements.txt
Train models
bash
Copy
Edit
# Train SVD model
python src/train.py

# Train item-based KNN model
python src/item_knn.py
Run the API
bash
Copy
Edit
uvicorn app.main:app --reload
Go to http://127.0.0.1:8000/docs for Swagger UI.

📮 API Endpoints
POST /recommend
Get top-N movie recommendations for a user.

json
Copy
Edit
{
  "user_id": 1,
  "n": 10
}
POST /similar
Get similar movies to a given movie name.

json
Copy
Edit
{
  "movie_name": "Godfather"
}
🧪 Run Tests
bash
Copy
Edit
pytest
🗃️ Dataset
Uses the MovieLens 10M Dataset.

⚠️ Notes
.pkl model files are large and may not be tracked by GitHub.

Add models manually or host them separately if deploying.

✨ Future Ideas
Add Streamlit frontend

Use Docker + Railway or Render for deployment

Add collaborative + content-based hybrid logic

vbnet
Copy
Edit

Let me know if you'd like to add things like project screenshots, badge shields, or deployment instructions
