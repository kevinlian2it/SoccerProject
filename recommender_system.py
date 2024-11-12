from clustering import cluster_players
from scoring import score_players_for_team
from model import train_recommender_system
import pandas as pd


# recommender_system.py
class RecommenderSystem:
    def __init__(self, player_data, team_data):
        # Initialize with player data, team data, and a trained model
        self.player_data = player_data
        self.team_data = team_data

        # Train the RandomForest model and save the feature columns used in training
        self.model, self.features_used = train_recommender_system(self.player_data)

    def recommend(self, team_name, position=None, top_n=5):
        # Score players for team suitability
        scored_players = score_players_for_team(self.player_data, self.team_data, team_name)

        scored_players = scored_players[scored_players['Squad'] != team_name]

        # Debug: Print the shape and head of scored_players before filtering by position
        #print(f"Scored players for {team_name} (before filtering by position):")
        #print(scored_players.head(), scored_players.shape)

        # Filter by position if specified
        if position:
            scored_players = scored_players[scored_players['Position'] == position]

        # Debug: Print the shape and head of scored_players after filtering by position
        #print(f"Scored players for {team_name} with position '{position}' (after filtering):")
        #print(scored_players.head(), scored_players.shape)

        # Check if scored_players is empty after filtering
        if scored_players.empty:
            print(f"No players found for team '{team_name}' with position '{position}'.")
            return pd.DataFrame()  # Return an empty DataFrame if no players match

        # Use only the columns that were used during training
        features = scored_players[self.features_used]

        # Check if features DataFrame is empty
        if features.empty:
            print("No features available for prediction. Check feature selection.")
            return pd.DataFrame()

        # Predict suitability scores
        scored_players['Predicted_Suitability'] = self.model.predict(features)

        # Sort players by predicted suitability and return top N
        recommendations = scored_players.sort_values(by='Predicted_Suitability').head(top_n)
        return recommendations[['Player', 'Nation', 'Squad', 'Age', 'Position', 'League', 'Predicted_Suitability']]
