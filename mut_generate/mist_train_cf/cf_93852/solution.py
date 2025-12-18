"""
QUESTION:
Write a function `count_occurrences(text, word)` that takes two parameters: `text` (a string) and `word` (a string). The function should count the occurrences of `word` in `text` while ignoring case sensitivity and only considering standalone occurrences (i.e., "lovely" should not be counted as an occurrence of "love"). The function should return the count of occurrences.
"""

def count_occurrences(text, word):
    text = text.lower()
    words = text.split()
    count = 0
    for w in words:
        if w == word.lower():
            count += 1
    return count