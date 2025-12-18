"""
QUESTION:
Write a function `convert_punctuation_to_text` that takes a string as input and returns the string with all occurrences of '.', ',', '!', and '?' replaced with ' period', ' comma', ' exclamation', and ' question' respectively. The replacement should not include extra spaces before or after the text phrases.
"""

def convert_punctuation_to_text(text):
    text = text.replace('.', ' period')
    text = text.replace(',', ' comma')
    text = text.replace('!', ' exclamation')
    text = text.replace('?', ' question')
    return text