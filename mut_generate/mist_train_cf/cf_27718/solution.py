"""
QUESTION:
Create a function `count_license_words(license_text: str) -> dict` that takes a multi-line string `license_text` as input, ignores punctuation marks, and returns a dictionary where the keys are unique words in the license text (converted to lowercase) and the values are the counts of each word.
"""

import re
from collections import Counter

def count_license_words(license_text: str) -> dict:
    cleaned_text = re.sub(r'[^\w\s]', '', license_text).lower()
    words = cleaned_text.split()
    return dict(Counter(words))