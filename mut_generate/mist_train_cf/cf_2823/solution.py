"""
QUESTION:
Implement a function `removeExtraWhitespace` that takes a string sentence as input and returns the modified sentence with all extra whitespace removed. The function must have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input sentence. The modified sentence should not contain any leading or trailing whitespace, and there should be exactly one whitespace character between each pair of words.
"""

def removeExtraWhitespace(sentence):
    # Remove leading and trailing whitespace
    sentence = sentence.strip()
    
    # Remove extra whitespaces between words
    words = sentence.split()
    return ' '.join(words)