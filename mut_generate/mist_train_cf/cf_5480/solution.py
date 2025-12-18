"""
QUESTION:
Write a Python function named `compare_strings` that compares two input strings. The function should take into account the difference between the '==' operator and the 'is' keyword when comparing strings. Also, consider the time complexity of the comparison methods and suggest an alternative method that may offer better performance.
"""

def compare_strings(str1, str2):
    """
    Compare two input strings using the '==' operator.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
    
    Returns:
        bool: True if the strings are equal, False otherwise.
    """
    return str1 == str2