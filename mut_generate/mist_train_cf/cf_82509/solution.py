"""
QUESTION:
Create a function called `most_common_words` that finds the n most frequent words and their counts in a string. The function should consider words with different cases as the same word (e.g. "Hello" and "hello" should be considered as the same word) and handle punctuation marks by considering words separated by a comma, period, or an exclamation mark as separate words. The function should take two parameters: `text` (the input string) and `n` (the number of most frequent words to return).
"""

import re
from collections import Counter

def most_common_words(text, n):
    words = re.findall(r'\b\w+\b', text.lower())
    most_common = Counter(words).most_common(n)
    return most_common