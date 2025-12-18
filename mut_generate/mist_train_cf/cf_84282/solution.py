"""
QUESTION:
Create a function called `reverse_words` that takes a string `s` as input and returns a string where the order of the words is reversed and each word is reversed. The function should handle multiple spaces between words and remove any leading or trailing spaces from the original string.
"""

def entrance(s):
    return ' '.join(word[::-1] for word in s.split()[::-1])