"""
QUESTION:
Create a function called `word_frequency` that takes a sentence as input, ignores punctuation marks, and considers words with different letter casing as the same word. The function should return a dictionary where the keys are the words in the sentence and the values are their corresponding frequencies.
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