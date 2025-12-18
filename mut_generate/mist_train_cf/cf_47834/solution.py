"""
QUESTION:
Write a function `rename_spike_columns` that takes a pandas DataFrame and a substring as input, renames the columns that contain the substring but do not exactly match it, to 'spike1', 'spike2', and so on, and returns the modified DataFrame. The substring must be an uninterrupted part of the column label.
"""

def rename_spike_columns(df, s):
    """
    Rename columns in a pandas DataFrame that contain a given substring but do not exactly match it.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame.
    s (str): Substring to search for in column names.
    
    Returns:
    pd.DataFrame: Modified DataFrame with renamed columns.
    """
    cols_with_spike = [col for col in df.columns if s in col and col != s]
    for i, col in enumerate(cols_with_spike, 1):
        df.rename(columns={col: f'spike{i}'}, inplace=True)
    return df