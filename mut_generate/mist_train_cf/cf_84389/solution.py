"""
QUESTION:
Write a function `generate_dict(text)` that takes a string `text` as input and returns a dictionary where each key is a distinct character from the string (ignoring case and punctuation), and each value is another dictionary containing the count of occurrences of the character and the index of its first occurrence in the string.
"""

from collections import Counter

def generate_dict(text):
    text_lc = text.lower()  # Ignore case
    counter = Counter(ch for ch in text_lc if ch.isalpha())  # Count occurrences and ignore punctuation
    result = {k: {'count': v, 'first_occurrence': text_lc.find(k)} for k, v in counter.items()}    
    return result