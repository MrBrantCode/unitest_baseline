"""
QUESTION:
Replace Informal Words in a Sentence

Write a function `replace_informal_words` that takes a sentence and a dictionary of informal words as input, where the dictionary's keys are the informal words and the dictionary's values are their corresponding formal alternatives. The function should return the sentence with all informal words replaced by their formal alternatives.
"""

def replace_informal_words(sentence, informal_words):
    """
    Replace informal words in a sentence with their formal alternatives.
    
    Args:
    sentence (str): The input sentence.
    informal_words (dict): A dictionary of informal words and their formal alternatives.
    
    Returns:
    str: The sentence with all informal words replaced.
    """
    for word in informal_words:
        sentence = sentence.replace(word, informal_words[word])
    return sentence