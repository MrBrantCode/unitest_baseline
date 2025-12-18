"""
QUESTION:
Implement a function `removeExtraWhitespace` that takes a string sentence as input and returns the modified sentence with all extra whitespace removed. The function should remove leading and trailing whitespace, and ensure there is exactly one whitespace character between each pair of words. The input sentence will only contain printable ASCII characters, and the function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input sentence.
"""

def removeExtraWhitespace(sentence):
    # Remove leading and trailing whitespace
    sentence = sentence.strip()
    
    # Remove extra whitespaces between words
    words = sentence.split()
    return ' '.join(words)