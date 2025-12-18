"""
QUESTION:
Develop a function `recurrence_rate(phrases, term)` that calculates the recurrence rate of a unique term within a collection of alphanumeric phrases. The function should take a list of phrases and a term as input, remove non-alphanumeric characters, convert to lower case, and return the recurrence rate of the term as the number of occurrences divided by the total number of words. If the term does not appear in the text, the function should return 0. The input phrases may contain punctuation and the comparison of words should be case-insensitive.
"""

from collections import Counter
import re

def recurrence_rate(phrases, term):
    total_text = ' '.join(phrases)
    total_text_clean = re.sub(r'\W+', ' ', total_text).lower()
    words = total_text_clean.split(' ')
    term_count = Counter(words)
    
    if term in term_count:
        return term_count[term] / len(words)
    else:
        return 0