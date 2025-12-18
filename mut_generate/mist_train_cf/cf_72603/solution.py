"""
QUESTION:
Create a function called `convert_punctuation` that takes a string `text` as input and returns the text with all punctuation marks converted to hyphens. The function should support the following punctuation marks: '.', ',', ':', ';', '!', '?', '(', ')', '\"', '\'', '\\', '/', ']', '[', '{', '}' and '|'. It should also convert multiple consecutive punctuation marks to a single hyphen. However, if the punctuation is an apostrophe in an English contracted word (e.g. "don't", "can't"), it should not be converted.
"""

import re

def convert_punctuation(text):
    contractions = re.findall(r"\w+'\w+", text)
    text = re.sub(r'[.,:;!()?\"\\\/\]\[\{\}\|]+', '-', text)
    for contraction in contractions:
        text = text.replace(contraction.replace("'", "-"), contraction)
    text = re.sub(r'\s-\s', ' ', text)
    return text