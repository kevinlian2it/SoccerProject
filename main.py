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

    # Prompt user to select a team
    team_names = team_processed_data['Squad'].tolist()
    print("Select a team for which you want recommendations:")
    for i, team_name in enumerate(team_names, 1):
        print(f"{i}. {team_name}")

    team_index = int(input("Enter the number for the team: ")) - 1
    selected_team = team_names[team_index]

    # Get user input for the position using abbreviations
    position_map = {'MF': 'Midfielder', 'FW': 'Forward', 'DF': 'Defender'}
    print("\nSelect a position for which you want recommendations:")
    print("MF for Midfielder, FW for Forward, DF for Defender")
    position_input = input("Enter the position abbreviation (leave blank for any): ").upper()
    position = position_map.get(position_input, None)

    # Step 3: Make Recommendations
    top_n = int(input("How many player recommendations do you want? "))
    recommendations = recommender.recommend(selected_team, position, top_n)

    # Display recommendations
    print(f"\nRecommendations for {selected_team} ({'any position' if not position else position}):")
    print(recommendations)

if __name__ == "__main__":
    main()
