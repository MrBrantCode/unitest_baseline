"""
QUESTION:
Create a function `word_dictionary(sentence)` that takes a string as input and returns a dictionary where the keys are the words in the sentence, and the values are dictionaries with two keys: 'Frequency' and 'Character count', representing the frequency of the word in the sentence and the number of characters in the word, respectively. The function should handle punctuation and special characters by removing them, and it should convert all words to lowercase for consistent counting.
"""

import collections
import re

def word_dictionary(sentence):
    # Remove punctuation and special characters in the string
    sentence = re.sub('[^A-Za-z0-9 ]+', '', sentence)
    
    # Convert to lowercase and split the sentence into words
    words = sentence.lower().split()
    
    # Count the occurrence of each word using a dictionary
    word_count = collections.Counter(words)
   
    # Create a new dictionary with word, frequency, and character count
    word_dict = {word: {'Frequency': freq, 'Character count': len(word)} for word, freq in word_count.items()}
    
    return word_dict