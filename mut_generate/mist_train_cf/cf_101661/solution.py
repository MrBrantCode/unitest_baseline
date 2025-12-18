"""
QUESTION:
Create a function called `word_lengths` that takes a string `sentence` as input and returns a dictionary where the keys are the words in the sentence and the values are the lengths of the corresponding words. The function should split the sentence into individual words and calculate the length of each word.
"""

def word_lengths(sentence):
    """
    This function takes a string sentence as input and returns a dictionary 
    where the keys are the words in the sentence and the values are the lengths 
    of the corresponding words.
    
    Parameters:
    sentence (str): The input sentence.
    
    Returns:
    dict: A dictionary with words as keys and their lengths as values.
    """
    words = sentence.split()
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    return word_lengths