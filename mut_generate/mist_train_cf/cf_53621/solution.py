"""
QUESTION:
Define a function called `predict_monsoon_advent` that determines whether predicting the advent date of the annual monsoon is best approached as a classification or regression problem based on the desired outcome.
"""

def predict_monsoon_advent(outcome):
    """
    This function determines whether predicting the advent date of the annual monsoon 
    is best approached as a classification or regression problem based on the desired outcome.

    Args:
        outcome (str): The desired outcome, either 'exact_date' for regression or 'category' for classification.

    Returns:
        str: The type of problem (classification or regression) that best suits the desired outcome.
    """
    if outcome == 'exact_date':
        return 'regression'
    elif outcome == 'category':
        return 'classification'
    else:
        return 'Invalid outcome. Please specify either exact_date or category.'