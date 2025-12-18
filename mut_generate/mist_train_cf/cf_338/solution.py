"""
QUESTION:
Write a function `convert_words` that takes an array of strings as input. The function should convert each word to uppercase if its length is greater than 5, then append the string "Welcome to the magnificent celebration" to the end of the resulting list. The function should return a string containing all the words from the list, separated by a space.
"""

def convert_words(words):
    """
    Converts words with more than 5 characters to uppercase and appends a celebratory message.

    Args:
        words (list): A list of strings.

    Returns:
        str: A string containing the modified words and the celebratory message.
    """
    output = [word.upper() if len(word) > 5 else word for word in words]
    output.append("Welcome to the magnificent celebration")
    return " ".join(output)