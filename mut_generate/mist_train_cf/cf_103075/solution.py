"""
QUESTION:
Write a function `invert_words` that takes a string of space-separated words as input and returns a new string with each word's characters in reverse order.
"""

def invert_words(string):
    words = string.split(" ")
    inverted_words = []
    
    for word in words:
        inverted_word = word[::-1]
        inverted_words.append(inverted_word)
    
    inverted_string = " ".join(inverted_words)
    return inverted_string