"""
QUESTION:
Create a function `last_two_upper` that takes a string as input and returns a new string where the last two characters of each word are transformed into uppercase. If a word has less than 2 characters, it should remain unchanged.
"""

def last_two_upper(s):
    return ' '.join(word[:-2] + word[-2:].upper() if len(word) >= 2 else word for word in s.split(" "))