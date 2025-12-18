"""
QUESTION:
Write a function named `match_pattern` that uses a regular expression to match variations of the sentence "an apple a day keeps the doctor away" with the following characteristics:
- The function is case-insensitive.
- It allows extra spaces between words.
- It allows substitution of the word "apple" with synonyms "fruit".
- It allows substitution of the word "doctor" with synonyms "physician" or "healthcare provider".
- It allows adding or removing punctuation marks.
- It allows pluralizing or singularizing words.
- It should match the entire word and not just parts of words.
"""

import re

def match_pattern(sentence):
    pattern = r"(?i)\b(an|a) (apple|fruit) (a|one) (day|daily) keeps? (the|a) (doctor|physician|healthcare provider)(s?) away\b"
    return bool(re.search(pattern, sentence))