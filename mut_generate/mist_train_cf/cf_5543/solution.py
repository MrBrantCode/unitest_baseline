"""
QUESTION:
Create a function named word_frequency that takes an input string and returns a dictionary containing the frequency of each word in the string, considering words as case-sensitive. The function should exclude any words that contain numbers or special characters.
"""

import re

def word_frequency(input_string):
    word_freq = {}
    input_string = re.sub(r'[^\w\s]', '', input_string)
    words = input_string.split()
    
    for word in words:
        if not any(char.isdigit() or not char.isalpha() for char in word):
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    
    return word_freq