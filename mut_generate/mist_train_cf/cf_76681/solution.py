"""
QUESTION:
Write a function named `filter_words` that takes two parameters: a string `s` and a target word. The string `s` contains words separated by commas, spaces, or both. The function should return a list of words in the original order, excluding all instances of the target word.
"""

def filter_words(s, target):
    """
    You'll receive a string of words, which may be separated by commas, spaces, or both. Your goal is to
    process the string into an array of words in the original order, but with all instances of a specified target word eliminated.
    
    Parameters:
    s (str): The input string of words
    target (str): The target word to be eliminated

    Returns:
    list: A list of words in the original order, excluding all instances of the target word
    """
    # Replace all commas with spaces to handle the given delimiters
    words = s.replace(',', ' ')

    # Split the string by spaces
    words = words.split()

    # Remove target word from list
    words = [word for word in words if word != target]

    return words