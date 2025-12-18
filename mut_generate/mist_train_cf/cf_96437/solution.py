"""
QUESTION:
Design a function called `reverse_words` that takes a string parameter. The function should remove any non-alphabet characters from the string, reverse the order of its words, and exclude any consecutive duplicate words.
"""

import re

def reverse_words(string):
    string = re.sub('[^a-zA-Z ]', '', string)  
    words = string.split()  
    words.reverse()  
    result = []
    previous_word = None
    for word in words:
        if word == previous_word:
            continue
        result.append(word)
        previous_word = word
    return ' '.join(result)  