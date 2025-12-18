"""
QUESTION:
Implement a function `reverse_words(message)` that takes a string of words as input and returns a new string where each word is reversed individually.
"""

def reverse_words(message):
    # Split the message into words
    words = message.split(' ')

    # Reverse each word and store them into a new list
    reversed_words = [word[::-1] for word in words]

    # Join the reversed words back into a string with spaces in between
    new_message = ' '.join(reversed_words)

    return new_message