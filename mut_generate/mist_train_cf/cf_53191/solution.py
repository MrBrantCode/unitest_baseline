"""
QUESTION:
Create a function called `to_uppercase` that takes a string as input and returns a new string where the first letter of every word is uppercase. The function should handle punctuation marks as part of the words.
"""

def to_uppercase(s):
    return ' '.join(word[0].upper() + word[1:] for word in s.split())