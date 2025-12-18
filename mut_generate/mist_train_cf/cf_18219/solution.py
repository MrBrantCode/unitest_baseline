"""
QUESTION:
Create a function `word_frequency(sentence)` that takes a sentence as input and returns a dictionary where the keys are the unique words in the sentence and the values are their frequencies. The function should ignore punctuation marks, consider words with different letter casing as the same word, and exclude common words such as articles, prepositions, and conjunctions.
"""

import string

def word_frequency(sentence):
    # Create a list of common words to exclude
    common_words = ['the', 'and', 'or', 'but', 'a', 'an', 'in', 'on', 'at', 'to', 'over', 'under', 'above', 'below', 'by']
    
    # Remove punctuation marks from the sentence
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    # Convert the sentence to lowercase
    sentence = sentence.lower()
    
    # Split the sentence into words
    words = sentence.split()
    
    # Create a dictionary to store word frequencies
    word_freq = {}
    
    # Iterate over each word
    for word in words:
        # Check if the word is not in the list of common words
        if word not in common_words:
            # If the word is already in the dictionary, increment its frequency
            if word in word_freq:
                word_freq[word] += 1
            # If the word is not in the dictionary, add it with a frequency of 1
            else:
                word_freq[word] = 1
    
    return word_freq