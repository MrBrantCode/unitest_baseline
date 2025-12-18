"""
QUESTION:
Create a function called `remove_special_characters` that takes a string as input and returns the string after removing all special characters, including underscores, without leaving any empty spaces in place of the removed characters.
"""

def remove_special_characters(text):
    import re
    pattern = re.compile('[\W_]+')
    text = pattern.sub('', text)
    return text