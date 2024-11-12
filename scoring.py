# scoring.py
import numpy as np
import pandas as pd

def score_players_for_team(player_data, team_data, target_team):
    """
    Scores each player based on their suitability for a target team.

    Args:
    player_data (pd.DataFrame): The DataFrame containing player statistics.
    team_data (pd.DataFrame): The DataFrame containing team statistics.
    target_team (str): The name of the target team.

    Returns:
    pd.DataFrame: The DataFrame with suitability scores for the target team.
    """
    # Get the target team's stats
    team_stats = team_data[team_data['Squad'] == target_team]
    if team_stats.empty:
        raise ValueError(f"Team {target_team} not found in team data.")

    # Define target values based on available stats in team data
    target_xG = pd.to_numeric(team_stats['xG'], errors='coerce').iloc[0]
    target_tkl_perc = pd.to_numeric(team_stats['Tkl%'], errors='coerce').iloc[0] if 'Tkl%' in team_stats else 0
    target_tkl_int = pd.to_numeric(team_stats['Tkl+Int'], errors='coerce').iloc[0] if 'Tkl+Int' in team_stats else 0

    # Ensure relevant columns in player_data are numeric, only if they exist
    for col in ['npxG', 'xAG', 'Tkl%', 'Tkl+Int']:
        if col in player_data.columns:
            player_data[col] = pd.to_numeric(player_data[col], errors='coerce').fillna(0)

    # Calculate suitability based on relevant stats
    def calculate_suitability(row):
        # Suitability is a combination of offensive and defensive suitability
        stat_diff = np.sqrt(
            (row.get('npxG', 0) - target_xG) ** 2 +
            (row.get('xAG', 0) - target_xG) ** 2 +
            (row.get('Tkl%', 0) - target_tkl_perc) ** 2 +
            (row.get('Tkl+Int', 0) - target_tkl_int) ** 2
        )
        return stat_diff

    # Apply suitability calculation to each player
    player_data['Suitability'] = player_data.apply(calculate_suitability, axis=1)
    return player_data
