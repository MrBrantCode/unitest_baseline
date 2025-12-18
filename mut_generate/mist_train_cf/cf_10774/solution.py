"""
QUESTION:
Write a function `reverse_words` that takes a string of alphabetic characters and spaces as input, reverses the order of the words, and then reverses the characters within each word. The output should maintain the same capitalization as the input.
"""

def reverse_words(string):
    words = string.split()
    words = words[::-1]
    reversed_words = [word[::-1] for word in words]
    reversed_string = ' '.join(reversed_words)
    return reversed_string