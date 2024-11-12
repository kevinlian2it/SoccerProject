# data_extraction.py
import pandas as pd


def scrape_data(player_url, defense_url):
    """
    Scrape player statistics data from two fbref.com URLs.

    Args:
    player_url (str): URL for general player stats (Forwards, Midfielders).
    defense_url (str): URL for defensive stats (Defenders, Midfielders).

    Returns:
    tuple: DataFrames for player stats and defense stats.
    """
    try:
        player_data = pd.read_html(player_url)[0]
        defense_data = pd.read_html(defense_url)[0]
        return player_data, defense_data
    except Exception as e:
        print(f"Error fetching player data: {e}")
        return pd.DataFrame(), pd.DataFrame()


def scrape_team_data(standard_url, defense_url):
    """
    Scrape team statistics data from two fbref.com URLs.

    Args:
    standard_url (str): URL for standard team stats.
    defense_url (str): URL for defensive team stats.

    Returns:
    pd.DataFrame: A combined DataFrame of team stats.
    """
    try:
        standard_data = pd.read_html(standard_url)[0]
        standard_data.columns = [col if isinstance(col, str) else col[1] for col in standard_data.columns]

        # Load the defensive team stats and flatten multi-level column names
        defense_data = pd.read_html(defense_url)[0]
        defense_data.columns = [col if isinstance(col, str) else col[1] for col in defense_data.columns]

        # Merge on 'Squad' to create a single team stats DataFrame
        team_data = pd.merge(standard_data, defense_data, on='Squad')

        return team_data
    except Exception as e:
        print(f"Error fetching team data: {e}")
        return pd.DataFrame()
