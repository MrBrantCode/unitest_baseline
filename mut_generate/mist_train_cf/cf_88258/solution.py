"""
QUESTION:
Write a function called `count_character` that takes two parameters: a string and a character. The function should return the number of times the given character appears in the string without using any built-in functions or methods that directly count the occurrences of the character. The solution must have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1).
"""

def count_character(string, char):
    """
    Counts the occurrences of a given character in a string.
    
    Args:
        string (str): The input string.
        char (str): The character to count.
    
    Returns:
        int: The number of occurrences of the character in the string.
    """
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count