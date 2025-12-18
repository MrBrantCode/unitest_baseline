"""
QUESTION:
Write a function `find_shortest_substring` that takes two parameters: a list of words and a string. The function should return the shortest word in the list that is a substring of the string. If no word in the list is a substring of the string, the function may return any value (it is not specified what the function should do in this case).
"""

def find_shortest_substring(words, string): 
    """
    Given an array containing words and a string, find the shortest word in the array that is a substring of the string.
    
    Parameters:
    words (list): A list of words.
    string (str): The string to check for substrings.
    
    Returns:
    str: The shortest word in the list that is a substring of the string.
    """
    min_length = float("inf")
    min_word = None
    for word in words:
        j = string.find(word)
        if j > -1 and len(word) < min_length:
            min_length = len(word)
            min_word = word
    return min_word