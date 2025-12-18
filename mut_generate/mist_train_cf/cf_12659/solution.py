"""
QUESTION:
Create a function named `filter_words` that takes a string as input and returns a list of words. The function should include only words that are longer than 5 characters and contain at least one uppercase letter.
"""

def filter_words(input_string):
    """
    This function takes a string as input, splits it into words, 
    and returns a list of words that are longer than 5 characters 
    and contain at least one uppercase letter.

    Args:
        input_string (str): The input string to be filtered.

    Returns:
        list: A list of words that meet the specified conditions.
    """
    return [word for word in input_string.split() if len(word) > 5 and any(letter.isupper() for letter in word)]