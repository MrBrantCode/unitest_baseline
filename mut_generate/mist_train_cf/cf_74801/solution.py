"""
QUESTION:
Create a function named `sophisticated_text_modification` that takes a string `input_text` and performs the following operations: 
1. Replace one or more successive blank spaces with a single space.
2. Replace one or more successive blank spaces (including the single space from step 1) with a hyphen if they are between words, or with an underscore if they are between a word and a non-word character, or if they are at the start or end of the string.
3. Convert all words within the string to their upper case form.
"""

import re

def sophisticated_text_modification(input_text):
    # Remove excess spaces
    input_text = re.sub(' +', ' ', input_text)

    # Split words
    words = input_text.split(' ')
    
    # Convert all words into upper case
    words = [word.upper() for word in words]

    # Join words with underscores
    input_text = '_'.join(words)
    
    # Replace two or more successive underscores with a hyphen
    input_text = re.sub('_+', '-', input_text)

    return input_text