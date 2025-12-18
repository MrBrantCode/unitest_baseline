"""
QUESTION:
Write a function `encode_missing_values` that handles missing values in a dataset where certain variables (e.g., turnover, assets, liabilities) are only applicable to companies and not authorized individuals. The function should take a Pandas DataFrame `df` as input and return the modified DataFrame with the missing values encoded in a way that is suitable for machine learning models such as logistic regression and random forests.

The function should assume that missing values are not due to data collection issues but rather a conceptual fact, and that the dataset has a variable indicating whether a client is a company or an authorized individual. The function should create new binary columns to capture the presence or absence of data and replace missing values with a fixed value.
"""

def encode_missing_values(df):
    """
    Encode missing values in a Pandas DataFrame by creating new binary columns 
    to capture the presence or absence of data and replacing missing values with a fixed value.

    Args:
        df (Pandas DataFrame): The input DataFrame containing missing values.

    Returns:
        Pandas DataFrame: The modified DataFrame with encoded missing values.
    """

    # Define the columns that have missing data due to clients being individual clients
    columns_with_missing_data = ['turnover', 'assets', 'liabilities']

    # Iterate over each column with missing data
    for column in columns_with_missing_data:
        # Create a new binary column to capture the presence or absence of data
        df[f'{column}_present'] = df[column].notna().astype(int)

        # Replace missing values with a fixed value (0 in this case)
        df[column] = df[column].fillna(0)

    return df