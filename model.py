# model_training.py
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd

def train_recommender_system(player_data):
    """
    Trains a RandomForest model to recommend players based on suitability scores.

    Args:
    player_data (pd.DataFrame): The DataFrame containing player statistics and suitability scores.

    Returns:
    tuple: A trained model and a list of features used.
    """
    player_data = player_data.apply(pd.to_numeric, errors='coerce').fillna(0)

    features = player_data[['npxG', 'xAG', 'PrgC', 'PrgP', 'Tkl%', 'Tkl+Int', 'Age']]
    target = player_data['Suitability']

    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    mse = mean_squared_error(y_test, model.predict(X_test))
    print(f"Mean Squared Error: {mse}")

    return model, features.columns.tolist()
