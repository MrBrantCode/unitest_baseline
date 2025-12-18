"""
QUESTION:
Write a function named `reverse_words_in_sentence` that takes a string sentence as input, reverses each word in the sentence while maintaining their original sequence, and returns the resulting string. The words are separated by a single space.
"""

def reverse_words_in_sentence(sentence):
    # Split the sentence into words
    words = sentence.split(' ')
    
    # Reverse each word and join them back into a sentence.
    reversed_sentence = ' '.join(word[::-1] for word in words)
    
    return reversed_sentence