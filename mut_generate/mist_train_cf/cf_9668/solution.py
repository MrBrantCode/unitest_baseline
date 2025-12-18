"""
QUESTION:
Create a function named `parse_string` that takes two parameters: a string `string` and a list of strings `stop_words`. The function should return a dictionary where the keys are the unique words from the input string (excluding words in `stop_words` and punctuation) and the values are their corresponding frequencies. The function should be case-insensitive when comparing the input string words with the stop words.
"""

import string

def parse_string(s, stop_words):
    word_freq = {}
    stop_words = [word.lower() for word in stop_words]
    translator = str.maketrans('', '', string.punctuation)
    
    words = s.translate(translator).lower().split()
    
    for word in words:
        if word not in stop_words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    
    return word_freq