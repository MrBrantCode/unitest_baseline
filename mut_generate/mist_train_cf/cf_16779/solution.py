"""
QUESTION:
Write a function `count_excluded_lowercase` that calculates the total number of lowercase characters in a given string, excluding any lowercase characters that are immediately preceded or followed by an uppercase character. The function should not consider the first and last characters of the string for the preceding and following conditions respectively.
"""

def count_excluded_lowercase(s):
    """
    Calculate the total number of lowercase characters in a given string, 
    excluding any lowercase characters that are immediately preceded or followed by an uppercase character.

    Parameters:
    s (str): The input string.

    Returns:
    int: The total number of excluded lowercase characters.
    """
    return sum(1 for i in range(1, len(s)-1) 
               if s[i].islower() and not s[i-1].isupper() and not s[i+1].isupper())