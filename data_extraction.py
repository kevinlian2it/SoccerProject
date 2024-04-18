import requests
from bs4 import BeautifulSoup
import pandas as pd
def scrape_data(url):
    """
        Scrape the player statistics data from a given fbref.com URL.

        Args:
        url (str): The URL to scrape data from.

        Returns:
        pd.DataFrame: A DataFrame containing scraped data.
        """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')  # Assuming we're looking for the first table
        df = pd.read_html(str(table))[0]
        return df
    else:
        print("Failed to retrieve data")
        return pd.DataFrame()
