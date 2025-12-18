"""
QUESTION:
Implement a function `vowels_count(s)` that calculates the total number of vowels in a given string `s`, considering only the English vowels 'a', 'e', 'i', 'o', 'u', and 'y' when 'y' is at the end of the string. The function should be case-insensitive and ignore special characters. It should also handle non-string inputs by returning an error message.
"""

def vowels_count(s):
    """
    Calculate the total number of vowels in a given string.

    This function considers only the English vowels 'a', 'e', 'i', 'o', 'u', 
    and 'y' when 'y' is at the end of the string. It is case-insensitive and 
    ignores special characters. Non-string inputs return an error message.

    Parameters:
    s (str): The input string.

    Returns:
    int: The total number of vowels in the string, or an error message if the input is not a string.
    """

    if not isinstance(s, str):
        return "Invalid input! Please provide a string."

    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    s = s.lower()
    count = sum(1 for char in s if char in vowels)
    if s and s[-1] == 'y':
        count += 1
    return count