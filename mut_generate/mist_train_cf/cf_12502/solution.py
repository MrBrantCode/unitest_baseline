"""
QUESTION:
Write a function `extract_word_in_parentheses` that takes two parameters: `text` and `word`. The function should return a list of all instances of the given `word` that are enclosed within parentheses in the `text`. The function should be case-sensitive and return an empty list if no instances are found.
"""

def extract_word_in_parentheses(text, word):
    """
    This function takes a text and a word as input, and returns a list of all instances 
    of the given word that are enclosed within parentheses in the text.

    Args:
        text (str): The input text to search for the word.
        word (str): The word to search for in the text.

    Returns:
        list: A list of instances of the word enclosed within parentheses.
    """

    result = []
    start = 0
    while True:
        start = text.find('(', start)
        if start == -1:
            break
        end = text.find(')', start)
        if end == -1:
            break
        if word in text[start+1:end]:
            result.append(word)
        start = end + 1

    return result