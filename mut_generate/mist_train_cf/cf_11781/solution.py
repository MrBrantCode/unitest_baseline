"""
QUESTION:
Create a function `to_camel_case` that takes a string as input. The function should convert the string to CamelCase if it contains at least one uppercase letter, otherwise return the original string. The conversion should be done by capitalizing the first letter of each word (separated by underscores) except the first word, which should remain unchanged.
"""

def to_camel_case(string):
    if any(letter.isupper() for letter in string):
        words = string.split('_')
        return words[0] + ''.join(word.capitalize() for word in words[1:])
    else:
        return string