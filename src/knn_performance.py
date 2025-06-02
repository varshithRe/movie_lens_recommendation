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
with open('models/item_knn_tuned.pkl', 'rb') as f:
    algo = pickle.load(f)

predictions = algo.test(testset)

test_rmse = accuracy.rmse(predictions)
test_mae = accuracy.mae(predictions)

#printing the performance
print(f"Model performance \nRMSE = {test_rmse:.5f}\nMAE = {test_mae:.5f}")

'''KNNBasic Model Performance on 10 million movielens dataset is 
RMSE = 1.06741
MAE = 0.85722
(Model is trained on 100k dataset)'''