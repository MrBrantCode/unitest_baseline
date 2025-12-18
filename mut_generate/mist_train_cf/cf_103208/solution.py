"""
QUESTION:
Write a function called `count_python_occurrences` that takes a string as an input and returns the total number of occurrences of the word 'Python' (considering both uppercase and lowercase occurrences) in the string. The input string can contain any combination of uppercase and lowercase letters, spaces, and punctuation.
"""

def count_python_occurrences(s):
    """
    This function counts the total number of occurrences of the word 'Python' 
    (considering both uppercase and lowercase occurrences) in a given string.

    Parameters:
    s (str): The input string to be searched for 'Python' occurrences.

    Returns:
    int: The total number of 'Python' occurrences in the input string.
    """
    return s.lower().count('python')