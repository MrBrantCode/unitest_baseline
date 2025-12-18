"""
QUESTION:
Write a function named `remove_and_reverse` that takes two parameters: a string and a character. The function should remove all occurrences of the character from the string in a case-sensitive manner, reverse the modified string, and return the result. The function should be able to handle multiple occurrences of the character.
"""

def remove_and_reverse(s, c):
    return s.replace(c, '')[::-1]