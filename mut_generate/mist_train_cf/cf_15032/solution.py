"""
QUESTION:
Write a function named `reverse_sentence` that takes a sentence as input. The function should return the reversed version of the sentence, ignoring any punctuation marks and special characters. It should also handle cases where multiple spaces are present between words, collapsing them into a single space.
"""

def reverse_sentence(sentence):
    # Remove punctuation marks and special characters
    cleaned_sentence = ''.join(c for c in sentence if c.isalpha() or c.isspace())
    
    # Remove extra spaces between words
    cleaned_sentence = ' '.join(cleaned_sentence.split())
    
    # Reverse the cleaned sentence
    reversed_sentence = cleaned_sentence[::-1]
    
    return reversed_sentence