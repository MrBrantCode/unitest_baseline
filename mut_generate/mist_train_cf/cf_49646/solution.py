"""
QUESTION:
Write a function named `handle_out_of_vocabulary` to handle words that are not in the vocabulary (Out-Of-Vocabulary or OOV words) during the training process of a Word2Vec model. The function should take in a word and a vocabulary as input and return a representation for the word, either by ignoring it, assigning a unique token, applying subword embedding methods, or other approaches. The function should not take any additional arguments other than the word and the vocabulary.
"""

def handle_out_of_vocabulary(word, vocabulary):
    """
    Handle words that are not in the vocabulary (Out-Of-Vocabulary or OOV words) 
    during the training process of a Word2Vec model.

    Args:
    word (str): The word to be handled.
    vocabulary (dict or list): The vocabulary of words.

    Returns:
    str: A representation for the word, either by ignoring it, assigning a unique token, 
    applying subword embedding methods, or other approaches.
    """
    
    # Strategy 1: Assign a unique token for all OOV words
    if word not in vocabulary:
        return '<UNK>'  # <UNK> is a common token for unknown words

    # If the word is in the vocabulary, return the word itself
    return word