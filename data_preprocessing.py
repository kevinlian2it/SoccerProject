# data_preprocessing.py
import pandas as pd


def preprocess_data(player_df, defense_df):
    """
    Preprocess the player and defense data to include relevant statistics.

    Args:
    player_df (pd.DataFrame): DataFrame containing player stats.
    defense_df (pd.DataFrame): DataFrame containing defensive stats.

    Returns:
    pd.DataFrame: The merged and processed player data with relevant stats.
    """
    # Flatten column names
    player_df.columns = [col[1] if isinstance(col, tuple) else col for col in player_df.columns]
    defense_df.columns = [col[1] if isinstance(col, tuple) else col for col in defense_df.columns]

    # Select relevant columns
    player_df = player_df[['Player', 'Nation', 'Pos', 'Comp', 'Squad', 'Age', '90s', 'npxG', 'xAG', 'npxG+xAG', 'PrgC', 'PrgP']]
    defense_df = defense_df[['Player', 'Nation', 'Pos', 'Comp', 'Squad', 'Age', '90s', 'Tkl%', 'Tkl+Int']]

    # Merge player and defense stats on common columns
    merged_df = pd.merge(player_df, defense_df, on=['Player', 'Nation', 'Pos', 'Comp', 'Squad', 'Age', '90s'], how='outer')

    merged_df['Comp'] = merged_df['Comp'].str.split().str[1:].str.join(' ')
    merged_df['Nation'] = merged_df['Nation'].str.split().str[1:].str.join(' ')

    # Handle duplicate columns if they exist
    merged_df = merged_df.loc[:, ~merged_df.columns.duplicated()]

    # Handle missing values
    merged_df = merged_df.fillna(0)

    merged_df = merged_df.rename(columns={
        'Pos': 'Position',
        'Comp': 'League'
    })

    # Convert 'Age' and other relevant columns to numeric for calculations
    merged_df['Age'] = merged_df['Age'].astype(str).str.split('-').str[0]

    return merged_df


def preprocess_team_data(team_data):
    """
    Preprocess the combined team data for relevant stats.

    Args:
    team_data (pd.DataFrame): The combined DataFrame of team stats.

    Returns:
    pd.DataFrame: Processed team stats DataFrame.
    """
    # Select only the relevant columns from the combined team data
    team_data = team_data[['Squad', 'xG', 'xGA', 'xGD/90', 'Tkl%', 'Tkl+Int']].copy()

    # Fill any missing values with 0
    team_data = team_data.fillna(0)

    return team_data