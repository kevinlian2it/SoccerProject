# app.py
from flask import Flask, request, jsonify
import pandas as pd
from recommender_system import RecommenderSystem
from data_preprocessing import preprocess_data, preprocess_team_data
from data_extraction import scrape_data, scrape_team_data
from scoring import score_players_for_team

app = Flask(__name__)

# URLs for player and team data
player_url = "https://fbref.com/en/comps/Big5/stats/players/Big-5-European-Leagues-Stats"
defense_url = "https://fbref.com/en/comps/Big5/defense/players/Big-5-European-Leagues-Stats"
team_standard_url = "https://fbref.com/en/comps/9/Premier-League-Stats#all_stats_squads_standard"
team_defense_url = "https://fbref.com/en/comps/9/defense/Premier-League-Stats"

def fetch_and_preprocess_data():
    player_data, defense_data = scrape_data(player_url, defense_url)
    processed_data = preprocess_data(player_data, defense_data)

    # Scrape and preprocess team data
    team_data = scrape_team_data(team_standard_url, team_defense_url)
    processed_team_data = preprocess_team_data(team_data)

    return processed_data, processed_team_data

# Fetch and preprocess data at the startup
player_data, team_data = fetch_and_preprocess_data()

@app.route('/api/recommend', methods=['GET'])
def recommend():
    # Get query parameters for team and position
    team = request.args.get('team')
    position = request.args.get('position')

    # Check if the parameters are provided
    if not team or not position:
        return jsonify({"error": "Team and position parameters are required"}), 400

    # Call the recommendation system
    try:
        scored_data = score_players_for_team(player_data.copy(), team_data, team)

        # Initialize RecommenderSystem with scored data
        recommender = RecommenderSystem(scored_data, team_data)

        recommendations = recommender.recommend(team, position, top_n=5)
        # Convert recommendations to JSON-serializable format
        recommendations_json = recommendations.to_dict(orient='records')
        return jsonify(recommendations_json)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
