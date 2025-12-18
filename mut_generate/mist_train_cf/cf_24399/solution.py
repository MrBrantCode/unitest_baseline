"""
QUESTION:
Create a function `consecutive_hash_followed_by_alphabets` that takes a string as input. The function should return `True` if the string contains two consecutive "#" symbols followed by four alphabetic characters, and `False` otherwise.
"""

def consecutive_hash_followed_by_alphabets(s):
    return bool(re.search(r'##[a-zA-Z]{4}', s))