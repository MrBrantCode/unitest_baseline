"""
QUESTION:
Create a function named `reverse_words` that takes a string as input, removes leading and trailing whitespace, removes punctuation marks and special characters, splits the string into words, reverses the order of the words, removes duplicate words, and returns the resulting string. The function should handle cases where the input string contains multiple spaces between words, and it should not include any duplicate words in the output.
"""

def reverse_words(string):
    # Remove leading and trailing whitespace
    string = string.strip()

    # Remove punctuation marks and special characters
    string = ''.join(c for c in string if c.isalnum() or c.isspace())

    # Split the string into a list of words
    words = string.split()

    # Reverse the order of the words
    words = words[::-1]

    # Remove duplicate words
    words = list(dict.fromkeys(words))

    # Join the words back into a string
    reversed_string = ' '.join(words)

    return reversed_string