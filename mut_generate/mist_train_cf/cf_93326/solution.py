"""
QUESTION:
Write a function `shortest_substring` that takes an array of words and a string as input and returns the shortest word in the array that is a substring of the string. The function should handle duplicates in the array and special characters/spaces in the string. If no word in the array is a substring of the string, the function's behavior is unspecified.
"""

def shortest_substring(words, string):
    """
    Returns the shortest word in the array that is a substring of the string.

    Args:
        words (list): A list of words.
        string (str): The string to search for substrings.

    Returns:
        str: The shortest word that is a substring of the string.
    """
    shortest_word = None
    shortest_length = float('inf')

    for word in words:
        if word in string and len(word) < shortest_length:
            shortest_word = word
            shortest_length = len(word)

    return shortest_word