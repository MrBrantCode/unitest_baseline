"""
QUESTION:
Write a function `count_one_letter_words` that takes a list of strings, where each string contains a single letter surrounded by spaces, and returns a dictionary where the keys are the letters and the values are the number of occurrences of each letter in the list. The function should handle an input list of any size and should return a dictionary with all unique letters found in the list as keys.
"""

from typing import List, Dict

def count_one_letter_words(words: List[str]) -> Dict[str, int]:
    letter_count = {}
    for word in words:
        letter = word.strip()  # Remove leading and trailing spaces
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count