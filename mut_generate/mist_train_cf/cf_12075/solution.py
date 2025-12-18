"""
QUESTION:
Write a function `capitalize_and_reverse` that takes a string as input, capitalizes all letters, and reverses the order of the words. The function should return a string with the modified words in reverse order.
"""

def capitalize_and_reverse(s):
    return ' '.join(word.upper()[::-1] for word in s.split(' ')[::-1])