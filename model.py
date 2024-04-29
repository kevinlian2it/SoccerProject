import pandas as pd

class RecommenderSystem:
    def __init__(self, player_data, team_data):
        self.player_data = player_data
        self.team_data = team_data

    def find_best_fit(self, team_name, position=None):
        # Filter team data for a specific team
        team = self.team_data[self.team_data['Squad'] == team_name]
        if team.empty:
            return f"The team {team_name} does not exist. Try a different name."

        # Define the team's needs based on GCA90 stats
        team_sca90 = pd.to_numeric(team.iloc[0]['SCA90'], errors='coerce')

        # If the value cannot be converted to numeric, handle it
        if pd.isnull(team_sca90):
            raise ValueError(f"SCA90 for {team_name} cannot be converted to a numeric type.")

        # Convert the '90s' column to numeric and filter for players with at least 10.0 '90s'
        self.player_data['90s'] = pd.to_numeric(self.player_data['90s'], errors='coerce')
        available_players = self.player_data.dropna(subset=['90s'])
        available_players = available_players[available_players['90s'] >= 10.0]

        # Filter players based on the position if provided
        if position:
            available_players = self.player_data[self.player_data['Position'] == position]
        else:
            available_players = self.player_data

        # Convert the 'SCA90' column to numeric
        available_players['SCA90'] = pd.to_numeric(available_players['SCA90'], errors='coerce')

        # Ensure there are no NaN values before comparison
        available_players = available_players.dropna(subset=['SCA90'])

        # Now perform the comparison
        suitable_players = available_players[available_players['SCA90'] >= (team_sca90/8)]

        # Sort players by GCA and pick top recommendations
        top_players = suitable_players.sort_values(by='SCA90', ascending=False)

        return top_players[['Player', 'Nation', 'Squad', 'Age', 'Position', 'League', 'SCA90']]

    def recommend(self, team_name, position=None, top_n=5):
        recommended_players = self.find_best_fit(team_name, position)
        print(recommended_players)
        return recommended_players.head(top_n)
