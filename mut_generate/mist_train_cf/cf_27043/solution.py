"""
QUESTION:
Write a function `count_word_occurrences` that calculates the total number of occurrences of a given word in a list of strings. The function should be case-insensitive, count partial matches, and treat special characters and punctuation marks as word boundaries. 

The function should take two parameters: `word` (the word to be searched) and `word_list` (the list of strings to be searched in). It should return the total count of occurrences of the word.
"""

from typing import List
import re

def count_word_occurrences(word: str, word_list: List[str]) -> int:
    word = word.lower()
    count = 0
    for sentence in word_list:
        sentence = re.sub(r'[^a-zA-Z\s]', '', sentence)  
        words = sentence.lower().split()
        for w in words:
            if word in w:
                count += 1
    return count