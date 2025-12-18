"""
QUESTION:
Write a function `countArabicWords` that takes a string `arabicText` as input and returns the number of words in the Arabic text. A word is defined as a sequence of Arabic characters separated by spaces or line breaks. The function should remove HTML tags and non-Arabic characters from the input string.
"""

import re

def countArabicWords(arabicText):
    # Remove HTML tags and non-Arabic characters
    cleaned_text = re.sub(r'<.*?>', '', arabicText)  # Remove HTML tags
    cleaned_text = re.sub(r'[^ء-ي\s]', '', cleaned_text)  # Remove non-Arabic characters except spaces

    # Split the cleaned text into words and count the number of words
    words = cleaned_text.split()
    return len(words)