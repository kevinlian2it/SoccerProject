from data_extraction import scrape_data
from data_preprocessing import preprocess_data

def main():
    # Define the URL of the data source
    url = "https://fbref.com/en/comps/Big5/gca/players/Big-5-European-Leagues-Stats#stats_gca"

    # Step 1: Extract Data
    print("Starting data extraction...")
    raw_data = scrape_data(url)
    if raw_data.empty:
        print("No data extracted.")
        return

    # Step 2: Preprocess Data
    print("Starting data preprocessing...")
    processed_data = preprocess_data(raw_data)
    if processed_data.empty:
        print("Data preprocessing failed.")
        return

    # Example of further actions: Print first few rows to verify output
    print("Processed Data:")
    print(processed_data.head())

if __name__ == "__main__":
    main()
