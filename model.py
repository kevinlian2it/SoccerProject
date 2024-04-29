import pandas as pd

class RecommenderSystem:
    """
    A system to recommend soccer players to teams based on goal-creating action (GCA) statistics.

    Attributes:
        player_data (DataFrame): A DataFrame containing player statistics.
        team_data (DataFrame): A DataFrame containing team statistics.
    """
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
        # Calculate the individual player target SCA90 as 1/4th of the team's SCA90
        target_sca90 = team_sca90 / 5

        # If the value cannot be converted to numeric, handle it
        if pd.isnull(team_sca90):
            raise ValueError(f"SCA90 for {team_name} cannot be converted to a numeric type.")

        # Convert the '90s' column to numeric and filter for players with at least 10.0 '90s'
        self.player_data['90s'] = pd.to_numeric(self.player_data['90s'], errors='coerce')
        available_players = self.player_data.dropna(subset=['90s'])
        available_players = available_players[available_players['90s'] >= 10.0]

        # Drop all players from the specified team
        available_players = available_players[available_players['Squad'] != team_name]

        # If position is specified, further filter players by position
        if position:
            available_players = available_players[available_players['Position'] == position]

        # Convert the 'SCA90' column to numeric
        available_players['SCA90'] = pd.to_numeric(available_players['SCA90'], errors='coerce')

        # Ensure there are no NaN values before comparison
        available_players = available_players.dropna(subset=['SCA90'])

        suitable_players = available_players
        # Sort players by how close they are to the target SCA90
        suitable_players['delta_from_target'] = (suitable_players['SCA90'] - target_sca90).abs()
        top_players = suitable_players.sort_values(by='delta_from_target')

        return top_players[['Player', 'Nation', 'Squad', 'Age', 'Position', 'League', 'SCA90']]

    def recommend(self, team_name, position=None, top_n=5):
        """
        Generates a list of top N player recommendations for a specified team and position.

        Args:
            team_name (str): The team for which to make recommendations.
            position (str, optional): The specific position to consider for recommendations. Defaults to None.
            top_n (int, optional): The number of top player recommendations to return. Defaults to 5.

        Returns:
            DataFrame: A DataFrame of the top N recommended players for the team and position.
        """
        recommended_players = self.find_best_fit(team_name, position)
        return recommended_players.head(top_n)
