"""
QUESTION:
Create a function named `reverse_words` that takes a string as input and returns a string where each word is in reverse order. The function should ignore any leading or trailing whitespace in the input string and handle cases where the input string contains punctuation marks and special characters by removing them, except for whitespace. Words are separated by a single space and there are no multiple consecutive spaces between words.
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