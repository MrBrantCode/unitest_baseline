"""
QUESTION:
Write a function named `remove_duplicates` that takes a sentence as input, removes all duplicate words, and returns the modified sentence in alphabetical order along with the total count of unique words. The function should split the sentence into words, consider case sensitivity, and exclude punctuation.
"""

def remove_duplicates(sentence):
    """
    This function takes a sentence as input, removes all duplicate words, 
    and returns the modified sentence in alphabetical order along with the total count of unique words.
    
    Parameters:
    sentence (str): The input sentence.
    
    Returns:
    tuple: A tuple containing the modified sentence and the total count of unique words.
    """
    words = sentence.split()
    unique_words = sorted(set(words))
    modified_sentence = " ".join(unique_words)
    unique_words_count = len(unique_words)
    return modified_sentence, unique_words_count