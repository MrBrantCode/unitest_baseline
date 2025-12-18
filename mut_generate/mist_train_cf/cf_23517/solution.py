"""
QUESTION:
Create a function `split_sentence_into_dict` that takes a sentence as input and returns a dictionary where the keys and values are the individual words from the sentence. The input sentence will contain only spaces as delimiters.
"""

def split_sentence_into_dict(sentence):
    """Return a dictionary where the keys and values are the individual words from the sentence."""
    return {word: word for word in sentence.split()}