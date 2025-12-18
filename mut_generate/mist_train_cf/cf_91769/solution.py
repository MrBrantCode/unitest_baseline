"""
QUESTION:
Create a function `word_frequency(sentence)` that takes a sentence as input and returns a dictionary where the keys are the unique words in the sentence (ignoring case and punctuation) and the values are their respective frequencies. The function should consider words with different letter casing as the same word and ignore all punctuation marks.
"""

import string

def word_frequency(sentence):
    # Remove punctuation marks from the sentence
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    
    # Convert all words to lowercase
    sentence = sentence.lower()
    
    # Split the sentence into individual words
    words = sentence.split()
    
    # Create an empty dictionary to store word frequencies
    frequency_dict = {}
    
    # Count the frequency of each word
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    
    return frequency_dict