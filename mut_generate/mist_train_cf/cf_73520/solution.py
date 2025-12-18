"""
QUESTION:
Write a function `get_abbr` that takes a pandas DataFrame `df` and a state name as input, and returns the corresponding abbreviation as a string. The DataFrame `df` has two columns: `State` and `Abbr`. Assume that the relationship between `State` and `Abbr` is one-to-one.
"""

def get_abbr(df, state):
    """
    This function takes a pandas DataFrame and a state name as input, 
    and returns the corresponding abbreviation as a string.
    
    Parameters:
    df (pandas DataFrame): A DataFrame with 'State' and 'Abbr' columns.
    state (str): The state name for which the abbreviation is required.
    
    Returns:
    str: The abbreviation of the given state.
    """
    return df.loc[df['State'] == state, 'Abbr'].values[0]