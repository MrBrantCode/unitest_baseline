"""
QUESTION:
Write a function named `compare_strings` that compares two input strings using both the '==' operator and the 'is' keyword. The function should return the results of both comparisons. The function must take two string parameters.
"""

def compare_strings(str1, str2):
    """
    This function compares two input strings using both the '==' operator and the 'is' keyword.
    
    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.
    
    Returns:
        tuple: A tuple containing the results of the '==' operator comparison and the 'is' keyword comparison.
    """
    return str1 == str2, str1 is str2