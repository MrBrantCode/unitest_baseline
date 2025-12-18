"""
QUESTION:
Write a function `count_word(string, word)` that takes a string and a word as input and returns the number of times the word appears in the string, excluding any occurrences of the word within parentheses. The comparison should be case-insensitive.
"""

def count_word(string, word):
    """
    Counts the number of occurrences of a word in a string, excluding occurrences within parentheses.
    
    Args:
        string (str): The input string.
        word (str): The word to be counted.
    
    Returns:
        int: The number of occurrences of the word in the string.
    """
    count = 0
    inside_parentheses = False
    current_word = ""
    for char in string:
        if char == "(":
            inside_parentheses = True
        elif char == ")":
            inside_parentheses = False
        elif char.isalpha():
            current_word += char.lower()
        elif not char.isalpha() and current_word == word.lower() and not inside_parentheses:
            count += 1
            current_word = ""
        elif not char.isalpha() and current_word != word.lower():
            current_word = ""
    if current_word == word.lower() and not inside_parentheses:
        count += 1
    return count