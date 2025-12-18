"""
QUESTION:
Create a function named `is_palindrome(sentence)` that takes a sentence as input and returns whether it is a palindrome or not, disregarding any spaces, punctuation, and capitalization. The function should return "The sentence is a palindrome." if the sentence is a palindrome and "The sentence is not a palindrome." otherwise.
"""

def is_palindrome(sentence):
    # Remove spaces and punctuation
    sentence = ''.join(char for char in sentence if char.isalnum())

    # Convert to lowercase
    sentence = sentence.lower()

    # Reverse the string
    reversed_sentence = sentence[::-1]

    # Check if it is equal to the original string
    if sentence == reversed_sentence:
        return "The sentence is a palindrome."
    else:
        return "The sentence is not a palindrome."