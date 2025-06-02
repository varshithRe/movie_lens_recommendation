#This is item based collaborative filter using KNN algorithm
import pickle
import pandas as pd
from surprise import KNNBasic, Dataset, Reader
from surprise.model_selection import GridSearchCV

#loading data
ratings = pd.read_csv('data/ratings.dat',
                      sep = '::',
                      engine= 'python',
                      header=None,
                      names = ['user_id', 'movie_id', 'rating', 'timestamp' ],
                      encoding='latin-1')

#wrapping data
reader = Reader(rating_scale=(1,5))
data = Dataset.load_from_df(ratings[['user_id', 'movie_id', 'rating']], reader)

trainset = data.build_full_trainset()#full data for later refitting

#tuning the model
'''param_grid = {
    'k': [10, 20, 40, 80],
    'sim_options': {
        'name': ['cosine', 'pearson'],
        "user_based": [False],
        "shrinkage": [0, 10, 30],
        "min_support": [1, 5, 10]
    }
}

gs = GridSearchCV(
    KNNBasic,
    param_grid,
    measures=['rmse'],
    cv=3,        
    n_jobs=-1,          
    joblib_verbose=1
)

gs.fit(data)

#getting the best parameters and best rmse score
best_params = gs.best_params
print("\nRetraining final KNN with best RMSE params:", best_params)
print('\n:Best RMSE score',gs.best_score )'''

'''These are the best parameters  {'k': 80, 'sim_options': {'name': 'pearson', 'user_based': False, 'shrinkage': 0, 'min_support': 10}'''
#RMSE score for the model is 'rmse': 0.9922801698356877

#reffiting the best model with full dataset
knn_final = KNNBasic(
    k=80,
    sim_options={
        "name": 'pearson',
        "user_based": False,
        "shrinkage": 0,
        "min_support": 10
    }
)
knn_final.fit(trainset)

with open("models/item_knn_tuned.pkl", "wb") as f:
    pickle.dump(knn_final, f)

print("Saved the best model")