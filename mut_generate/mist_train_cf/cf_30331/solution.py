"""
QUESTION:
Create a function `word_frequency` that takes a list of strings as input and returns a dictionary where the keys are unique words and the values are their frequencies. The function should ignore case sensitivity and remove any non-alphabetic characters from the words before counting their frequency. The input list may contain words with non-alphabetic characters, and the function should handle this by stripping them from the words.
"""

from typing import List, Dict
import re

def word_frequency(words: List[str]) -> Dict[str, int]:
    word_count = {}
    for word in words:
        cleaned_word = re.sub(r'[^a-zA-Z]', '', word).lower()
        if cleaned_word:
            word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1
    return word_count