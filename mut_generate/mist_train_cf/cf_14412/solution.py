"""
QUESTION:
Create a function called `modify_sentence` that takes a string as input, replaces any invalid punctuation at the end of the string with a valid one (period, question mark, or exclamation mark), and returns the modified string. A valid punctuation is one that maintains the original meaning and grammatical sense of the sentence. If the original string already ends with a valid punctuation, the string should remain unchanged.
"""

def modify_sentence(sentence):
    """
    Replaces any invalid punctuation at the end of the string with a valid one.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: The modified sentence with valid punctuation.
    """
    valid_punctuation = ['.', '?', '!']
    if sentence[-1] not in valid_punctuation:
        if sentence[-1].isalnum():
            sentence += '.'
        else:
            sentence = sentence.rstrip(sentence[-1]) + '!'
    return sentence