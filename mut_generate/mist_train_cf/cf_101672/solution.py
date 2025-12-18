"""
QUESTION:
Write a function called `reverse_sentence(sentence)` that takes a string of words as input and returns a new string with the order of words reversed. The function should preserve the original words but change their order to be in reverse.
"""

def reverse_sentence(sentence):
    words = sentence.split() 
    reversed_words = words[::-1] 
    reversed_sentence = " ".join(reversed_words) 
    return reversed_sentence