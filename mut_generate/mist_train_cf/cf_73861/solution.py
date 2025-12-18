"""
QUESTION:
Replace all special characters and whitespace in a given sentence with their Unicode values, excluding those in a provided list of exceptions. The function should be efficient in handling this transformation. The function, named `transform_string`, takes two parameters: the input sentence and a list of exceptions. It should preserve alphanumeric characters and exceptions, but replace other characters with their Unicode values.
"""

def transform_string(sentence, exceptions):
    """
    Replaces special characters and whitespace in a sentence with their Unicode values,
    excluding characters in the provided list of exceptions.

    Args:
        sentence (str): The input sentence to be transformed.
        exceptions (list): A list of characters to be preserved in the output.

    Returns:
        str: The transformed sentence with replaced special characters and whitespace.
    """
    result = ""
    for char in sentence:
        if char.isalnum() or char in exceptions:
            result += char
        else:
            result += str(ord(char))
    return result