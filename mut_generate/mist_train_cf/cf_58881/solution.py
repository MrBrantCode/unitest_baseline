"""
QUESTION:
Create a function `to_camel_case` that transforms a given phrase into camel case. The input can be either a string or a list of strings, where each string can contain uppercase and lowercase alphabets, numbers, and special characters. The function should correctly handle strings and lists, and convert words separated by spaces, hyphens, or underscores to camel case.
"""

def to_camel_case(text):
    if isinstance(text, list):  
        text = ' '.join(text)
    text = ''.join(e for e in text if e.isalnum() or e in '-_ ').replace('-', ' ').replace('_', ' ').split(' ')
    return text[0].lower() + ''.join(i.capitalize() for i in text[1:])