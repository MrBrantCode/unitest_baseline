"""
QUESTION:
Write a function `reverse_words` that takes a string of alphabetic characters and spaces as input, ignores leading or trailing spaces, handles multiple consecutive spaces between words, and returns a string where each word's characters are reversed while maintaining the original word order.
"""

def reverse_words(string):
    # Remove leading and trailing spaces
    string = string.strip()

    # Split the string into a list of words
    words = string.split()

    # Reverse each word in the list
    reversed_words = [word[::-1] for word in words]

    # Join the reversed words back together
    reversed_string = ' '.join(reversed_words)

    return reversed_string