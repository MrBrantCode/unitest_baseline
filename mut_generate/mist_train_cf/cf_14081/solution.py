"""
QUESTION:
Create a function named `remove_extra_whitespace` that takes a string `sentence` as input, removes extra white spaces from the sentence, and returns the modified sentence along with the number of words in the sentence. The function should not take any other parameters.
"""

def remove_extra_whitespace(sentence):
    """
    Removes extra white spaces from the input sentence and returns the modified sentence along with the number of words.

    Args:
        sentence (str): The input sentence.

    Returns:
        tuple: A tuple containing the modified sentence and the number of words.
    """
    modified_sentence = ' '.join(sentence.split())
    word_count = len(modified_sentence.split())
    return modified_sentence, word_count