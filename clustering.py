# clustering.py
from sklearn.cluster import KMeans
import pandas as pd

def cluster_players(df, n_clusters=5):
    """
    Clusters players based on their statistics.

    Args:
    df (pd.DataFrame): The DataFrame containing player statistics.
    n_clusters (int): Number of clusters for KMeans.

    Returns:
    pd.DataFrame: The DataFrame with an added cluster label for each player.
    """
    # Select relevant features for clustering
    features = df[['SCA90', 'GCA90', 'Age', '90s']].copy()
    features = features.apply(pd.to_numeric, errors='coerce').fillna(0)

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Cluster'] = kmeans.fit_predict(features)

    return df
