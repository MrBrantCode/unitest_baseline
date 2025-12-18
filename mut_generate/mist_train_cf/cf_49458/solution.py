"""
QUESTION:
Write a function `sortAscii(s)` that takes a string `s` as input and returns the string with characters in each word sorted in ascending order based on their ASCII value, while maintaining the original word order. The function should handle all ASCII characters, not just alphabets.
"""

def sortAscii(s):
    words = s.split(' ')
    sorted_words = [''.join(sorted(word)) for word in words]
    return ' '.join(sorted_words)