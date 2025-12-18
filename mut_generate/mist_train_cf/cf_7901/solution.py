"""
QUESTION:
Create a function `modify_paragraph` that takes a string `paragraph` as input and returns a modified string. The function should replace all instances of "the" with "a", all instances of "is" with "was", and remove all punctuation marks. The modified string should still be grammatically correct and maintain the original meaning.
"""

import string

def modify_paragraph(paragraph):
    """
    This function takes a string paragraph as input, replaces 'the' with 'a', 'is' with 'was', 
    and removes punctuation marks to return a modified string.

    Args:
        paragraph (str): The input string to be modified.

    Returns:
        str: The modified string.
    """

    # Replace 'the' with 'a'
    modified_paragraph = paragraph.replace("the", "a")
    
    # Replace 'is' with 'was'
    modified_paragraph = modified_paragraph.replace("is", "was")

    # Remove punctuation marks
    modified_paragraph = modified_paragraph.translate(str.maketrans('', '', string.punctuation))

    return modified_paragraph