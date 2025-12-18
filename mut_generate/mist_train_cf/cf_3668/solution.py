"""
QUESTION:
Create a function named `sort_unique_words` that takes a string as input, removes punctuation marks, converts to lowercase, and returns a sorted list of unique words. The input string length is restricted to a maximum of 200 characters. The function should have a time complexity of O(n log n) and a space complexity of O(m), where n is the number of words and m is the number of unique words in the input string.
"""

import string

def sort_unique_words(input_string):
    input_string = input_string.translate(str.maketrans('', '', string.punctuation))
    input_string = input_string.lower()
    words = input_string.split()
    unique_words = set(words)
    sorted_words = sorted(unique_words)
    return sorted_words