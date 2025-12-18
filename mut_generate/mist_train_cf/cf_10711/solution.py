"""
QUESTION:
Reverse the words of a given sentence in-place in O(n) time complexity without using any built-in string manipulation functions, preserving leading and trailing spaces and handling multiple consecutive spaces between words. Implement a function named `reverse_words(sentence)` that takes a sentence as input and returns the reversed sentence.
"""

def reverse_words(sentence):
    # Convert the sentence to a list of characters
    sentence = list(sentence)
    
    # Reverse the entire sentence
    reverse_string(sentence, 0, len(sentence) - 1)
    
    # Reverse each word in the sentence
    start = 0
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            reverse_string(sentence, start, i - 1)
            start = i + 1
    
    # Reverse the last word in the sentence
    reverse_string(sentence, start, len(sentence) - 1)
    
    # Convert the list of characters back to a string
    return ''.join(sentence)

def reverse_string(string, start, end):
    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1