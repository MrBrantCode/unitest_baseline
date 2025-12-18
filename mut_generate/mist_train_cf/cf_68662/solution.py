"""
QUESTION:
Write a function `log_transformation_necessity` to determine if log transformation of independent variables is necessary in logistic regression. The function should take into account that the log of odds in logistic regression transforms probability values to a range across the whole real line, potentially revealing linear relationships, but does not necessarily address data issues such as skewness and heteroscedasticity.
"""

def log_transformation_necessity(is_skewed, is_heteroscedastic):
    """
    Determine if log transformation of independent variables is necessary in logistic regression.
    
    Parameters:
    is_skewed (bool): Whether the data is skewed.
    is_heteroscedastic (bool): Whether the data has non-constant variance.
    
    Returns:
    bool: True if log transformation is necessary, False otherwise.
    """
    return is_skewed or is_heteroscedastic