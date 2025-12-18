"""
QUESTION:
Create a function `remove_non_alphanumeric` that takes a string as input and returns a new string with all non-alphanumeric characters removed. The function should consider alphanumeric characters as alphabets (both lowercase and uppercase) and numbers.
"""

def remove_non_alphanumeric(string):
    return ''.join(c for c in string if c.isalnum())