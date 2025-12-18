"""
QUESTION:
Create a function `count_words` that generates a dictionary containing unique words in a given string of text and their occurrence counts, ignoring special characters, abbreviations, and acronyms, while considering the words in a case-insensitive manner. The function should optimize for both space and time complexity. The set of abbreviations and acronyms to ignore includes "btw" and "lol".
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