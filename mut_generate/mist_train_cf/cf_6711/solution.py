"""
QUESTION:
Create a function named `count_words` that takes a string of text as input and returns a dictionary containing the unique words in the text and their frequencies, ignoring special characters, abbreviations, and acronyms. The function should be case-insensitive and optimize for both space and time complexity. The set of abbreviations and acronyms to ignore is defined as {"btw", "lol"}.
"""

import re
from collections import Counter

def count_words(text):
    # Remove special characters and convert to lowercase
    cleaned_text = re.sub(r"[^\w\s]", "", text.lower())
    # Split the text into words
    words = cleaned_text.split()
    # Define a set of abbreviations and acronyms to ignore
    ignore = set(["btw", "lol"])
    # Count the occurrences of each word
    word_counts = Counter(word for word in words if word not in ignore)
    return word_counts