"""
QUESTION:
Write a function named `shared_elements` that takes three dictionaries `C`, `D`, and `E` as input. The function should return a dictionary containing all key-value pairs that are common to `C`, `D`, and `E`. Use dictionary comprehension to implement this function.
"""

def shared_elements(C, D, E):
    """
    Returns a dictionary containing all key-value pairs that are common to C, D, and E.
    
    Args:
    C (dict): The first dictionary.
    D (dict): The second dictionary.
    E (dict): The third dictionary.
    
    Returns:
    dict: A dictionary containing all key-value pairs common to C, D, and E.
    """
    return {key: C[key] for key in C if (key in D and D[key] == C[key]) and (key in E and E[key] == C[key])}