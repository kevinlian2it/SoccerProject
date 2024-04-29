from data_extraction import scrape_data
from data_preprocessing import preprocess_data
from preprocess_teams import preprocess_team
from model import RecommenderSystem

def main():
    # URL of the data source
    player_url = "https://fbref.com/en/comps/Big5/gca/players/Big-5-European-Leagues-Stats#stats_gca"
    team_url = "https://fbref.com/en/comps/9/gca/Premier-League-Stats"

    # Step 1: Extract Data
    print("Starting data extraction...")
    player_data = scrape_data(player_url)
    if player_data.empty:
        print("No data extracted.")
        return
    team_data = scrape_data(team_url)

    # Step 2: Preprocess Data
    print("Starting data preprocessing...")
    player_processed_data = preprocess_data(player_data)
    if player_processed_data.empty:
        print("Data preprocessing failed.")
        return
    team_processed_data = preprocess_team(team_data)

    # Initialize recommender system
    recommender = RecommenderSystem(player_processed_data, team_processed_data)

    # Step 3: Make Recommendations
    recommendations = recommender.recommend('Manchester City', position='Forward', top_n=5)

    # Display recommendations
    print("Recommendations for Man City (Midfielders):")
    print(recommendations)

if __name__ == "__main__":
    main()
