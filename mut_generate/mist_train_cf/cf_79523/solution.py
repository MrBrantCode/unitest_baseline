"""
QUESTION:
Write a function `is_t_distribution_statement_correct` that takes a statement about t-distributions as input and returns `True` if the statement is correct and `False` otherwise. The statements are: 
A) "The variance of t-distributions varies with different values of degrees of freedom."
B) "The distribution of t-distributions is both symmetric and bell-shaped."
C) "It's universally true for t-distributions to always have a mean of 0 and a standard deviation of 1."
D) "Compared to a normal distribution, a t-distribution will usually have more dispersion."
"""

def is_t_distribution_statement_correct(statement):
    """
    This function checks if a given statement about t-distributions is correct.
    
    Args:
    statement (str): The statement to be checked.
    
    Returns:
    bool: True if the statement is correct, False otherwise.
    """
    
    # Define the correct statements
    correct_statements = {
        "A": "The variance of t-distributions varies with different values of degrees of freedom.",
        "B": "The distribution of t-distributions is both symmetric and bell-shaped.",
        "D": "Compared to a normal distribution, a t-distribution will usually have more dispersion."
    }
    
    # Check if the statement is in the correct statements
    return statement in correct_statements.values()