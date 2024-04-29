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

    # Creating a list with new names
    new_columns = []
    for col in df.columns:
        if 'level_0' in col:
            new_col = col.split()[-1]  # takes the last name
        else:
            new_col = col
        new_columns.append(new_col)

    # Rename columns
    df.columns = new_columns
    df = df.fillna(0)

    # Clean specific columns
    df['Age'] = df['Age'].str[:2]
    df['Position_2'] = df['Pos'].str[3:]
    df['Position'] = df['Pos'].str[:2]
    df['Nation'] = df['Nation'].str.split(' ').str.get(1)
    df['League'] = df['Comp'].str.split(' ').str.get(1) + ' ' + df['Comp'].str.split(' ').str.get(2)
    df = df.drop(columns=['Comp', 'Rk', 'Pos', 'Matches'])

    # Map abbreviated positions to full names
    positions_map = {'MF': 'Midfielder', 'DF': 'Defender', 'FW': 'Forward', 'GK': 'Goalkeeper'}
    df['Position'] = df['Position'].map(positions_map)
    df['Position_2'] = df['Position_2'].map(positions_map)

    # Fill NA values for 'League' with default value if any
    df['League'] = df['League'].fillna('Bundesliga')

    df = df.rename(columns={
        'SCA SCA': 'SCA',
        'SCA SCA90': 'SCA90',
        'SCA Types PassLive': 'SCA PassLive',
        'SCA Types PassDead': 'SCA PassDead',
        'SCA Types TO': 'SCA TO',
        'SCA Types Sh': 'SCA Sh',
        'SCA Types Fld': 'SCA Fld',
        'SCA Types Def': 'SCA Def',
        'GCA GCA': 'GCA',
        'GCA GCA90': 'GCA90',
        'GCA Types PassLive': 'GCA PassLive',
        'GCA Types PassDead': 'GCA PassDead',
        'GCA Types TO': 'GCA TO',
        'GCA Types Sh': 'GCA Sh',
        'GCA Types Fld': 'GCA Fld',
        'GCA Types Def': 'GCA Def',
    })

    return df