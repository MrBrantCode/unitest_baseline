"""
QUESTION:
Write a function named `reverse_sentence` that takes a sentence as input and returns the sentence with the letters in each word reversed.
"""

def reverse_sentence(sentence):
    words = sentence.split()  
    reversed_words = [word[::-1] for word in words]  
    reversed_sentence = " ".join(reversed_words)  
    return reversed_sentence