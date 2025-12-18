"""
QUESTION:
Create a function called `create_ascii_dict` that takes a string `phrase` as input and returns a dictionary where the keys are the individual characters from the phrase and the values are the ASCII values of those characters. The function should consider all characters including spaces and punctuation, and it should only include unique characters from the phrase.
"""

def create_ascii_dict(phrase):
    """
    Create a dictionary where the keys are the individual characters 
    from the phrase and the values are the ASCII values of those characters.

    Args:
    phrase (str): The input string.

    Returns:
    dict: A dictionary with unique characters from the phrase as keys 
          and their ASCII values as values.
    """
    return {char: ord(char) for char in phrase}