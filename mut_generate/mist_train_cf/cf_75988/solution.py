"""
QUESTION:
Replace missing values in 'Income' column with the average income based on 'Education' level.

Create a function named `fill_income_na` that takes a DataFrame as input, replaces missing values in the 'Income' column with the average income for each 'Education' level, and returns the modified DataFrame.
"""

def fill_income_na(df):
    """
    Replaces missing values in the 'Income' column with the average income for each 'Education' level.

    Args:
        df (DataFrame): Input DataFrame.

    Returns:
        DataFrame: Modified DataFrame with missing 'Income' values replaced.
    """
    df['Income'] = df.groupby("Education")['Income'].transform(lambda x: x.fillna(x.mean()))
    return df