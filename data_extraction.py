import pandas as pd

def scrape_data(url):
    """
    Scrape the player statistics data from a given fbref.com URL using Pandas.

    Args:
    url (str): The URL to scrape data from.

    Returns:
    pd.DataFrame: A DataFrame containing scraped data.
    """
    try:
        # Fetch the HTML tables from the URL
        df = pd.read_html(url)[0]
        return df
    except Exception as e:
        print(f"An error occurred while fetching data: {e}")
        return pd.DataFrame()

