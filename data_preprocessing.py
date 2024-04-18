import pandas as pd

def preprocess_data(df):
    """
    Clean and preprocess the scraped data to remove multi-index and customize data frame.

    Args:
    df (pd.DataFrame): The DataFrame to preprocess.

    Returns:
    pd.DataFrame: The preprocessed DataFrame.
    """
    if df.empty:
        print("No data to process.")
        return df

    # Flatten the multi-level column headers
    df.columns = [' '.join(col).strip() for col in df.columns]
    df = df.reset_index(drop=True)

    # Rename columns and remove unwanted levels or prefixes
    df = df.rename(columns=lambda x: x.split(' ')[-1] if 'level_0' in x else x)

    # Clean specific columns
    df['Age'] = df['Age'].str[:2]
    df['Position_2'] = df['Pos'].str[3:]
    df['Position'] = df['Pos'].str[:2]
    df['Nation'] = df['Nation'].str.split(' ').str.get(1)
    df['League'] = df['Comp'].str.split(' ').str.get(1) + ' ' + df['Comp'].str.split(' ').str.get(2)
    df = df.drop(columns=['League_', 'Comp', 'Rk', 'Pos', 'Matches'])

    # Map abbreviated positions to full names
    positions_map = {'MF': 'Midfielder', 'DF': 'Defender', 'FW': 'Forward', 'GK': 'Goalkeeper'}
    df['Position'] = df['Position'].map(positions_map)
    df['Position_2'] = df['Position_2'].map(positions_map)

    # Fill NA values for 'League' with default value if any
    df['League'] = df['League'].fillna('Bundesliga')

    return df