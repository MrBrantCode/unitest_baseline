"""
QUESTION:
Write a function called `analyze_string` that takes a string of characters as input and returns a dictionary containing the frequency of each unique character (excluding whitespace and punctuation) in descending order of frequency.
"""

import string
from collections import OrderedDict

def analyze_string(input_string):
    frequencies = {}
    
    cleaned_string = input_string.translate(str.maketrans("", "", string.whitespace + string.punctuation))
    
    for char in cleaned_string:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    
    sorted_frequencies = OrderedDict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True))
    
    return sorted_frequencies