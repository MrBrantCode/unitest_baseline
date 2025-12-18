"""
QUESTION:
Write a function called `count_char_pairs` that takes two parameters: a string `text` and a string `pair` representing a sequence of two characters. The function should return the number of times the `pair` appears in `text` as adjacent characters. The function should only count non-overlapping occurrences of the `pair`.
"""

def count_char_pairs(text, pair):
    count = sum(1 for i in range(len(text)-1) if text[i:i+2] == pair)
    return count