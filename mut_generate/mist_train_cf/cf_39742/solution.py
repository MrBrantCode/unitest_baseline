"""
QUESTION:
Create a function `count_matched_words` that takes a sentence and a pattern as input, and returns a dictionary containing the matched words as keys and their respective counts as values. The pattern is a sequence of one or more word characters (alphanumeric or underscore) possibly followed by hyphens or apostrophes, and enclosed in triple quotes. The function should be case sensitive and match the words exactly as they appear in the sentence.
"""

import re

def count_matched_words(sentence: str, pattern: str) -> dict:
    compiled_pattern = re.compile(pattern)
    matched_words = compiled_pattern.findall(sentence)
    word_counts = {}
    for word in matched_words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts