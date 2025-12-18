"""
QUESTION:
Create a function named `to_camel_case` that takes a string as input and returns the string in camelCase format. The input string can be any textual string. The function should have a computational complexity of O(n), where n is the length of the input string.
"""

def to_camel_case(text):
    words = text.split(' ')
    result = ''
    for i, word in enumerate(words):
        if i == 0:
            result += word.lower()
        else:
            result += word.capitalize()
    return result