"""
QUESTION:
Write a function called `reverse_words` that takes a string of alphabetical characters and spaces as input, reverses the order of the words while maintaining their original spelling, removes leading and trailing spaces, and collapses multiple consecutive spaces into a single space. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1).
"""

def reverse_words(string):
    # Remove leading and trailing spaces
    string = string.strip()

    # Split the string into a list of words
    words = string.split()

    # Reverse the order of the words
    reversed_words = words[::-1]

    # Join the reversed words into a string
    reversed_string = ' '.join(reversed_words)

    return reversed_string