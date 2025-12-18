"""
QUESTION:
Write a function to convert a string into Camel and Pascal casing. The function should take a string as input, split it into words (assuming the words in the string are separated by a single space or underscore), capitalize the first letter of each word, and then combine the words into a single string. For Camel case, the first word should be in lower case, while for Pascal case, all words should start with a capital letter. The function should handle strings without spaces or underscores as a single word.
"""

def entrance(text):
    """
    Converts a string into both Camel and Pascal casing.

    Args:
    text (str): The input string to be converted.

    Returns:
    tuple: A tuple containing the Camel case and Pascal case strings.
    """
    
    # Split the input text into words using both space and underscore as separators
    words = text.lower().replace('_', ' ').split(' ')

    # Convert the words to Camel case
    camel_case = words[0] + ''.join(word.title() for word in words[1:])

    # Convert the words to Pascal case
    pascal_case = ''.join(word.title() for word in words)

    return camel_case, pascal_case