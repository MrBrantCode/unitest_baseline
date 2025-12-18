"""
QUESTION:
Capitalize the first letter of the first word after each period in a given text string. The function should be named `capitalize_after_period`. The input string can contain multiple sentences and the function should return the modified string.
"""

def capitalize_after_period(text):
    sentences = text.split('. ')
    sentences = [sentence.strip().capitalize() for sentence in sentences]
    return '. '.join(sentences)