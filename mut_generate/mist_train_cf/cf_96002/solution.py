"""
QUESTION:
Write a function `reverse_words` that takes a string as input, removes leading and trailing whitespace, and reverses the order of words while ignoring punctuation marks and special characters. The function should return the modified string with words in reverse order, separated by a single space.
"""

def reverse_words(s):
    # Remove leading and trailing whitespace
    s = s.strip()

    # Remove punctuation marks and special characters except whitespace
    s = ''.join(char for char in s if char.isalnum() or char.isspace())

    # Split the string into words
    words = s.split()

    # Reverse the order of words
    words.reverse()

    # Join the reversed words into a single string
    reversed_string = ' '.join(words)

    return reversed_string