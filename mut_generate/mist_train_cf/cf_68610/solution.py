"""
QUESTION:
Given a string of words, create a function named `find_repeated_word` that returns the first repeated word in a given string.
"""

def find_repeated_word(text):
    words = text.lower().split()
    word_counts = {}
    for word in words:
        word = ''.join(e for e in word if e.isalnum())
        if word in word_counts:
            return word
        else:
            word_counts[word] = 1
    return None