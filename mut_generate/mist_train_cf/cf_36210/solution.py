"""
QUESTION:
Create a Python function `process_text` that takes a string as input and returns the processed text with all punctuation marks removed and converted to lowercase. The input text will consist of alphabets, digits, and various punctuation marks. The function should not use any built-in Python functions for removing punctuation or converting to lowercase.
"""

def process_text(text: str) -> str:
    punc_remove = ['!', '.', ',', '?', ';', ':', '-', '"', "'", '(', ')']
    processed_text = ""
    for char in text:
        if char not in punc_remove:
            if 'A' <= char <= 'Z':
                char = chr(ord(char) + 32)
            processed_text += char
    return processed_text