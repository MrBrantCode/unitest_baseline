"""
QUESTION:
Write a function named `reverse_sentence` that takes a string sentence as input, reverses the order of words while maintaining the order of characters within each word, removes any leading or trailing white spaces, and does not use any built-in string manipulation functions or libraries. The input sentence will only contain spaces and alphabetic characters.
"""

def reverse_sentence(sentence):
    # remove leading and trailing white spaces
    sentence = sentence.strip()
    
    # split the sentence into words
    words = sentence.split()
    
    # reverse the order of words
    words = words[::-1]
    
    # join the words back into a sentence
    reversed_sentence = ' '.join(words)
    
    return reversed_sentence