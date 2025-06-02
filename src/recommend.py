import pickle
import pandas as pd
from surprise import SVD

#loading the data
with open('models/best_svd_model.pkl', 'rb') as f:
    algo: SVD = pickle.load(f)

movies = pd.read_csv('data/movies.dat', sep = '::', 
                     engine = 'python',
                     header = None, names = ['movie_id', 'title', 'genres'],
                     encoding = 'latin-1')

all_ids = movies['movie_id'].tolist()

#gives n movies 
def get_top_n(user_id: int, n:int = 10) -> list[str]:

#converting user_id to surprise internal id
    try:
        inner_uid = algo.trainset.to_inner_uid(user_id)
    except:
        raise ValueError(f"Unknown user id: {user_id}")
    
    #getting all movies seen by user
    seen = {iid for (iid, _) in algo.trainset.ur[inner_uid]}

#pred is a list of movie ids and its predicted rating that are not seen by user
    pred = [
        (mov_id, algo.predict(user_id, mov_id).est)
        for mov_id in all_ids if mov_id not in seen
    ]

#soring pred in descending order of predicted rating
    top_n = sorted(pred, key=lambda x: x[1], reverse = True)[:n]

#returning a list of n movie titles that user might like
    return [movies.set_index('movie_id').loc[mov_id, 'title'] for 
            mov_id, _ in top_n]

