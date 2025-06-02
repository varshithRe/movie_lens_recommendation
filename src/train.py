import pandas as pd
import pickle
from surprise import Dataset, Reader
from surprise import SVD, accuracy
from surprise.model_selection import GridSearchCV

ratings = pd.read_csv(
    r"d:\ml_projects\movie_lens recom\data\ratings.dat",
    sep="::",
    engine="python",
    header=None,
    names=["user_id", "movie_id", "rating", "timestamp"],
    encoding="latin-1"
)
print(ratings.head())

#dataframe to surprise dataset
reader = Reader(rating_scale=(1, 5))
surprise_data = Dataset.load_from_df(ratings[['user_id', 'movie_id', 'rating']], reader)


param_grid = {
    'n_factors' :[50, 100, 150],
    'n_epochs': [20,30,40],
    'lr_all': [0.002, 0.005],
    'reg_all': [0.02, 0.05, 0.1],
    'random_state' : [40]

}

#finding best model
gs = GridSearchCV(SVD, param_grid=param_grid, measures = ['rmse', 'mae'], cv=5, n_jobs =-1, joblib_verbose = 1)


gs.fit(surprise_data)

best_params = gs.best_params['rmse']
print("Best hyperparameters (RMSE):", best_params)

#retaining on full data so that we can get predictions for every user
algo = SVD(**best_params)
full_trainset = surprise_data.build_full_trainset()
algo.fit(full_trainset)



# Save the trained model
with open("models/best_svd_model.pkl", "wb") as f:
    pickle.dump(algo, f)

print("Model training complete. Saved to best_svd_model.pkl")

