"""
QUESTION:
Create a function called `build_word_frequency` that takes two inputs: a string and a list of stop words. The function should return a dictionary containing the frequency of each word in the string, ignoring punctuation, converting all words to lowercase, and excluding the provided stop words. If the input string is empty or contains only punctuation marks after stripping, return an error message instead.
"""

import string

def build_word_frequency(input_string, stop_words):
    if not input_string or input_string.strip(string.punctuation).strip() == '':
        return "Error: Input string is empty or contains only punctuation marks."
    
    input_string = input_string.lower().translate(str.maketrans('', '', string.punctuation))
    words = input_string.split()
    words = [word for word in words if word not in stop_words]
    
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    return word_freq