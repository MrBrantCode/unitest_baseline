"""
QUESTION:
Create a function called `analyze_string` that takes a string of characters as input, excludes whitespace and punctuation, and returns a dictionary with the number of occurrences of each unique character in descending order of frequency. The input string will only contain lowercase and uppercase letters, and special characters such as accents, diacritics, and umlauts should be accurately counted.
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