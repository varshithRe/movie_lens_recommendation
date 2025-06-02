import pickle
import pandas as pd
from surprise import Dataset, Reader, KNNBasic

with open('models/item_knn_tuned.pkl', 'rb') as f:
    algo: KNNBasic = pickle.load(f)

movies = pd.read_csv('data/movies.dat',
                      sep='::',
                      engine='python',
                      header= None,
                      names = ["movie_id", "title", "genres"],
                      encoding = 'latin-1')

#building surprise dataset
reader = Reader(rating_scale=(1,5))
ratings = pd.read_csv('data/ratings.dat',
                      sep='::',
                      engine='python',
                      header= None,
                      names = ['user_id', 'movie_id', 'rating', 'timestamp'],
                      encoding = 'latin-1')
data = Dataset.load_from_df(ratings[['user_id', 'movie_id', 'rating']], reader)
trainset = data.build_full_trainset()   #so that id mapping works correctly

def get_similar_movies(movie_name:str) ->list[str]:
    
    matches = movies[movies['title'].str.contains(movie_name, case=False, regex=False)] #getting a dataframe that has movie name substring entererd

    if matches.empty:
        raise ValueError(f"No movie found matching '{movie_name}'")
    
    raw_id = int(matches.iloc[0]['movie_id']) #getting the movie id of first movie from matches dataframe

    #converting raw id to surprise internal id
    try:
        inner_id = trainset.to_inner_iid(raw_id)
    except:
        raise ValueError(f"Movie id is not in trainset '{raw_id}'")
    
    #finding top 6 closest neighbours inner id
    inner_neighbours = algo.get_neighbors(inner_id, 6)

    raw_neighbours = [trainset.to_raw_iid(id) for id in inner_neighbours]

    return [
        movies.set_index('movie_id').loc[m_id, 'title']
        for m_id in raw_neighbours
    ]
