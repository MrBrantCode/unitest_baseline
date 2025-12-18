"""
QUESTION:
Write a function `split_string` that takes a string as input and splits it into a list of words. The function should handle multiple spaces, leading and trailing spaces, punctuation marks (commas, periods, exclamation marks), words with hyphens or apostrophes, and different types of whitespace characters. The function should also handle error cases where the input is empty or not a string, and return an error message in such cases.
"""

def split_string(s):
    # Error handling for empty or non-string input
    if not s or not isinstance(s, str):
        return "Error: Input string is empty or not a string."

    # Removing leading and trailing spaces
    s = s.strip()

    # Removing punctuation marks
    s = s.replace(',', '').replace('.', '').replace('!', '')

    # Handling multiple spaces and different types of whitespace characters
    s = ' '.join(s.split())

    # Handling words with hyphens or apostrophes
    s = s.replace('-', ' ').replace("'", ' ')

    # Splitting the string into words
    words = s.split()

    return words