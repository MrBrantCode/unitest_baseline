"""
QUESTION:
Write a function `count_word_occurrences(text, word)` that takes a text string and a word as input, and returns the number of occurrences of the word in the text string excluding occurrences inside single-quoted strings.
"""

import re

def count_word_occurrences(text, word):
    pattern = r"\b{}\b".format(word)
    matches = re.findall(pattern, text)

    def is_inside_quoted_string(start_index):
        quote_count = 0
        for i in range(start_index):
            if text[i] == "'":
                quote_count += 1
        return quote_count % 2 == 1

    return sum(1 for match in matches if not is_inside_quoted_string(text.index(match)))