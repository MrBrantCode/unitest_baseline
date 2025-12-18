"""
QUESTION:
Create a function `retrieve_info(text)` that takes a string as input. If the string contains commas or colons, return a list of words separated by these characters. If the string does not contain commas or colons, return the count of lower-case alphabetic characters with an odd index (where 'a' is 0, 'b' is 1, ..., 'z' is 25).
"""

def retrieve_info(text):
    if ',' in text:
        return text.split(',')
    elif ':' in text:
        return text.split(':')
    else:
        return sum(c.islower() and (ord(c) - ord('a')) % 2 for c in text)