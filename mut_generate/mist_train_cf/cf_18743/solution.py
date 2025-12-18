"""
QUESTION:
Write a function called `reverse_and_remove_duplicates` that takes a string of text as input, reverses the order of words, removes duplicates while preserving the original order of characters within each word, and returns the result as a string.
"""

def reverse_and_remove_duplicates(text):
    words = text.split()  
    reversed_words = list(reversed(words))  
    unique_words = list(dict.fromkeys(reversed_words))  
    result = ' '.join(unique_words)  
    return result