"""
QUESTION:
Create a function called `count_word_frequency` that takes a string of text as input. The function should first remove common words (articles, conjunctions, prepositions) from the text, then count the frequency of each unique word (ignoring case and non-alphabetic characters), and finally return a dictionary where the keys are the unique words and the values are their corresponding frequencies.
"""

import re
from collections import Counter

def count_word_frequency(text):
    common_words = ['the', 'of', 'and', 'a', 'to', 'in', 'is', 'you', 'that', 'it', 'he', 'was', 'for', 'on', 'are', 'as', 'with', 'his', 'they', 'I']
    pattern = r'\b(?:{})\b'.format('|'.join(common_words))
    text = re.sub(pattern, '', text, flags=re.IGNORECASE)
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = Counter(words)
    return word_count