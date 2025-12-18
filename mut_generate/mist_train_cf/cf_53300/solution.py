"""
QUESTION:
Create a function named `word_occurrence_count` that takes a sentence as input and returns a dictionary where each key is a word in the sentence and its corresponding value is the occurrence count of that word. The function should be case-sensitive and ignore punctuation marks, treating them as part of a word only when they are attached to it, but excluding them as standalone words.
"""

import string

def word_occurrence_count(sentence):
    """
    This function takes a sentence as input and returns a dictionary where each key is a word in the sentence 
    and its corresponding value is the occurrence count of that word. The function is case-sensitive and 
    ignores punctuation marks, treating them as part of a word only when they are attached to it, but 
    excluding them as standalone words.

    Args:
        sentence (str): Input sentence

    Returns:
        dict: A dictionary where each key is a word in the sentence and its corresponding value is the 
        occurrence count of that word.
    """
    translator = str.maketrans('', '', string.punctuation)
    sentence = sentence.translate(translator)
    words = sentence.split()
    
    words_dict = {}
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
            
    return words_dict