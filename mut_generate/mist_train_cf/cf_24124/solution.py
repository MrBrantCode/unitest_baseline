"""
QUESTION:
Write a function named `most_frequent_letter` that takes a string `s` as input and returns the most frequent letter in the string. The function should be case-sensitive and consider only alphabetic characters. If there are multiple letters with the same highest frequency, return any of them.
"""

def most_frequent_letter(s):
    """
    Returns the most frequent letter in the string.
    
    The function is case-sensitive and considers only alphabetic characters.
    If there are multiple letters with the same highest frequency, it returns any of them.

    Parameters:
    s (str): The input string.

    Returns:
    str: The most frequent letter in the string.
    """

    # Create a dictionary to store frequency of each letter
    freq_map = {}

    # Loop through the string
    for c in s:
        # Update the frequency map
        if c.isalpha():
            freq_map[c] = freq_map.get(c, 0) + 1

    # Find the letter with the highest frequency
    max_letter = max(freq_map, key=freq_map.get)

    return max_letter