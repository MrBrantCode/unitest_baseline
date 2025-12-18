"""
QUESTION:
Given a Python array of strings where each string represents a word in a sentence, write a function `retrieve_word` that takes the array and a negative index as input and returns the word at the specified index. The function should demonstrate the significance of a negative index in a Python array.
"""

def retrieve_word(sentence, index):
    """
    Retrieves the word at a specified negative index from a sentence.

    Args:
        sentence (list): A list of strings representing words in a sentence.
        index (int): A negative index specifying the word to retrieve.

    Returns:
        str: The word at the specified negative index.

    Raises:
        IndexError: If the index is out of range.
    """
    return sentence[index]