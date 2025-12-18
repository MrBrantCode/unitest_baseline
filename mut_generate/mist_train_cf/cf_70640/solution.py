"""
QUESTION:
Create a function `check_indictment` that takes a pandas Series `indictment_charges` as input and returns a new pandas Series `orc_4` where the value is `1` if the string '2907.04' is found in the corresponding value of `indictment_charges`, and `0` otherwise.
"""

import pandas as pd

def check_indictment(indictment_charges):
    """
    Creates a new pandas Series 'orc_4' where the value is 1 if the string '2907.04' 
    is found in the corresponding value of 'indictment_charges', and 0 otherwise.

    Parameters:
    indictment_charges (pd.Series): The input Series to be checked.

    Returns:
    pd.Series: A new Series 'orc_4' with the results.
    """
    return indictment_charges.apply(lambda x: 1 if '2907.04' in str(x) else 0)