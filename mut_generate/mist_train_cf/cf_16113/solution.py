"""
QUESTION:
Create a function `word_frequency` that takes a string as input and returns a dictionary with the frequency of each word excluding a predefined list of stop words. The function should convert all words to lowercase, ignore punctuation marks and numbers, and consider only the words that are not in the stop words list. The stop words list includes 'the', 'and', 'or', 'is', 'a', 'how', 'are', 'you', 'doing', 'today', 'weather', 'nice'.
"""

import string

def word_frequency(input_string):
    """
    Returns a dictionary with the frequency of each word excluding a predefined list of stop words.
    
    Parameters:
    input_string (str): The input string for which the word frequency is to be calculated.
    
    Returns:
    dict: A dictionary with words as keys and their frequencies as values.
    """
    stop_words = ['the', 'and', 'or', 'is', 'a', 'how', 'are', 'you', 'doing', 'today', 'weather', 'nice']
    frequency = {}
    translator = str.maketrans('', '', string.punctuation)
    words = input_string.lower().translate(translator).split()
    for word in words:
        if word not in stop_words and word.isalpha():
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
    return frequency