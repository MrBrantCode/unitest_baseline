"""
QUESTION:
Write a function `get_longest_sentence` that takes a string `text` as input, where the text contains one or more sentences separated by '. '. The function should return the length of the longest sentence in the given text. The sentences are separated by '. ' and do not contain any other punctuation marks.
"""

def get_longest_sentence(text):
    """
    This function calculates the length of the longest sentence in a given text.
    
    Args:
    text (str): A string containing one or more sentences separated by '. '.
    
    Returns:
    int: The length of the longest sentence in the given text.
    """
    sentences = text.split('. ')
    longest_sent_len = max(len(sentence) for sentence in sentences)
    return longest_sent_len