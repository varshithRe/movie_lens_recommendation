from surprise import Dataset, Reader, accuracy
import pickle
import pandas as pd
from surprise.model_selection import train_test_split

ratings = pd.read_csv("data/ratings10m.dat", sep="::",
                      engine="python", header=None,
                      names=["user_id","movie_id","rating","timestamp"],
                      encoding="latin-1")

#wraping dataframe in a surprise dataset
reader = Reader(rating_scale=(1,5))
data = Dataset.load_from_df(ratings[['user_id', 'movie_id', 'rating']], reader)

#train test split
trainset, testset = train_test_split(data, test_size = 0.2, random_state = 40)

#loading model
with open('models/best_svd_model.pkl', 'rb') as f:
    algo = pickle.load(f)

predictions = algo.test(testset)

test_rmse = accuracy.rmse(predictions)
test_mae = accuracy.mae(predictions)

#printing the performance
print(f"Model performance \nRMSE = {test_rmse:.5f}\nMAE = {test_mae:.5f}")
'''
Model performance on movielens 100k data set(as it is trained on)
RMSE = 0.70984
MAE = 0.56276

Model performance on movielens 10 Million dataset
RMSE = 0.98506
MAE = 0.77027'''