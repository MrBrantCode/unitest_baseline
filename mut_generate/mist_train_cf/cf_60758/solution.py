"""
QUESTION:
Write a function named `reverse_words` that takes a string of words as input and returns a string where each word is reversed, while maintaining their original order.
"""

def reverse_words(sentence):
    words = sentence.split(' ')        
    reversed_words = [word[::-1] for word in words]    
    reversed_sentence = ' '.join(reversed_words)    
    return reversed_sentence