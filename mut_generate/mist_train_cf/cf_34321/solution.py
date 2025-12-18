"""
QUESTION:
Create a function called `count_word_occurrences` that calculates the total number of occurrences of a given word in a list of strings. The function should be case-insensitive and count partial matches as well. The function takes two parameters: `word` (a string) and `word_list` (a list of strings), and returns the total count of occurrences as an integer.
"""

from typing import List

def count_word_occurrences(word: str, word_list: List[str]) -> int:
    count = 0
    word = word.lower()  # Convert the word to lowercase for case-insensitive comparison
    for item in word_list:
        item = item.lower()  # Convert each item in the list to lowercase
        if word in item:
            count += 1
    return count