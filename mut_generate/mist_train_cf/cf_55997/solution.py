"""
QUESTION:
Create a function `word_occurrence_dict` that takes a sentence as input and returns a dictionary where each key is a word from the sentence and its corresponding value is the occurrence count of that word. The function should consider case sensitivity and punctuation as part of the word, and split the sentence into words based on space characters.
"""

from collections import defaultdict

def word_occurrence_dict(sentence):
    """
    This function takes a sentence as input and returns a dictionary where each key is a word 
    from the sentence and its corresponding value is the occurrence count of that word.
    
    Args:
        sentence (str): Input sentence.
    
    Returns:
        dict: A dictionary with words as keys and their occurrence count as values.
    """
    word_occurrence_dict = defaultdict(int)
    
    for word in sentence.split():
        word_occurrence_dict[word] += 1
    
    return dict(word_occurrence_dict)