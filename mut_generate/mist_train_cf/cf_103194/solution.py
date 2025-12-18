"""
QUESTION:
Create a function `sort_words_by_length` that takes a sentence as input and returns a list of words sorted by their length in descending order. The input sentence is a string of words separated by spaces, and the output should be a list of strings where the longest words come first.
"""

def sort_words_by_length(sentence):
    words = sentence.split()  
    sorted_words = sorted(words, key=lambda x: len(x), reverse=True)  
    return sorted_words