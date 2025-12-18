"""
QUESTION:
Write a function `count_word_occurrences` that takes two parameters: a text string `text` and a word `word`. The function should return the number of occurrences of `word` in `text`, excluding any occurrences that are inside single-quoted strings.
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

        if quote_count % 2 == 1:
            return True

        return False

    count = 0
    for match in matches:
        start_index = text.index(match)
        if not is_inside_quoted_string(start_index):
            count += 1

    return count