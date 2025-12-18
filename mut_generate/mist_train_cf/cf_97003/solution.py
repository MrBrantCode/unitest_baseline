"""
QUESTION:
Write a function named `count_words` that takes a string as input and returns the number of words in the string, excluding any occurrences of "test" and its variations. The function should have a time complexity of O(n), where n is the length of the string.
"""

def count_words(s):
    """
    Counts the number of words in a string, excluding "test" and its variations.

    Args:
        s (str): The input string.

    Returns:
        int: The number of words in the string, excluding "test" and its variations.
    """
    words = s.split()
    return sum(1 for word in words if word.lower() not in ["test", "testing", "tested"])