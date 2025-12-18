"""
QUESTION:
Write a function called replace_word() that replaces all occurrences of the word "apple" with the word "fruit" in a given sentence. The replacement should be case-insensitive.
"""

def replace_word(sentence):
    """
    Replaces all occurrences of the word "apple" with the word "fruit" in a given sentence.
    The replacement is case-insensitive.
    
    Args:
        sentence (str): The input sentence.
    
    Returns:
        str: The sentence with "apple" replaced by "fruit".
    """
    return sentence.replace('apple', 'fruit').replace('Apple', 'fruit')