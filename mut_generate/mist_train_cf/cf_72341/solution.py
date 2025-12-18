"""
QUESTION:
Write a function `extract_after_last_underscore` that takes a pandas Series of strings as input, extracts everything after the last underscore in each string, and returns the modified Series. If a string does not contain an underscore, it should remain unchanged.
"""

def extract_after_last_underscore(series):
    """
    This function takes a pandas Series of strings as input, extracts everything 
    after the last underscore in each string, and returns the modified Series. 
    If a string does not contain an underscore, it should remain unchanged.

    Parameters:
    series (pandas Series): A pandas Series of strings.

    Returns:
    pandas Series: The modified Series with everything after the last underscore in each string.
    """
    return series.apply(lambda x: x.split('_')[-1] if '_' in x else x)