"""
QUESTION:
Implement a function named `is_palindrome` that takes a sentence as input and returns a boolean indicating whether the sentence is a palindrome, ignoring non-alphanumeric characters and case differences. The function should consider a sentence a palindrome if, after removing all non-alphanumeric characters and converting to lowercase, the resulting string is equal to its reverse.
"""

def is_palindrome(sentence):
    # Remove all non-alphanumeric characters from the sentence
    sentence = ''.join(filter(str.isalnum, sentence.lower()))
    
    # Check if the sentence is equal to its reverse
    return sentence == sentence[::-1]