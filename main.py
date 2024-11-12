# main.py
from data_extraction import scrape_data, scrape_team_data
from data_preprocessing import preprocess_data, preprocess_team_data
from scoring import score_players_for_team
from recommender_system import RecommenderSystem

def main():
    # URLs for player stats and defensive stats
    player_url = "https://fbref.com/en/comps/Big5/stats/players/Big-5-European-Leagues-Stats"
    defense_url = "https://fbref.com/en/comps/Big5/defense/players/Big-5-European-Leagues-Stats"

    # URLs for team standard and defense stats
    team_standard_url = "https://fbref.com/en/comps/9/Premier-League-Stats#all_stats_squads_standard"
    team_defense_url = "https://fbref.com/en/comps/9/defense/Premier-League-Stats"

    # Scrape and preprocess player data
    player_data, defense_data = scrape_data(player_url, defense_url)
    processed_data = preprocess_data(player_data, defense_data)

    # Scrape and preprocess team data
    team_data = scrape_team_data(team_standard_url, team_defense_url)
    processed_team_data = preprocess_team_data(team_data)
    print(processed_team_data)


    # Calculate suitability scores
    target_team = "Chelsea"  # Example team
    processed_data = score_players_for_team(processed_data, processed_team_data, target_team)

    # Initialize the recommender system
    recommender = RecommenderSystem(processed_data, processed_team_data)

    # Generate and display recommendations
    recommendations = recommender.recommend(target_team, position="MF", top_n=5)
    print(recommendations)

if __name__ == "__main__":
    main()
