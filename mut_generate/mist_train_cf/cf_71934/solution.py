"""
QUESTION:
Create a function `reflect(s)` that takes a string `s` as input, reverses the order of words, and returns the resulting string while maintaining the individual characters in each word in their original order.
"""

def reflect(s):
    words = s.split()  # split the string into words
    reversed_words = words[::-1]  # reverse the order of words
    reflected_str = ' '.join(reversed_words)  # join the words back into a string
    return reflected_str