"""
QUESTION:
Write a function `find_longest_word` that takes a sentence as input and returns the length and the longest word in the sentence. The input sentence is a string containing multiple words separated by spaces, and the function should handle this input accordingly.
"""

def find_longest_word(sentence):
    words = sentence.split()
    max_len = 0
    longest_word = ""

    for word in words:
        if (len(word) > max_len):
            max_len = len(word)
            longest_word = word
    
    return max_len, longest_word