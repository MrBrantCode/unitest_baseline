"""
QUESTION:
Design a function called `count_word_occurrences` that takes two parameters: a string `sentence` and a string `word`. The function should be case-insensitive and return the number of times `word` occurs in `sentence`.
"""

def count_word_occurrences(sentence, word):
    sentence = sentence.lower()
    word = word.lower()
    words = sentence.split()
    count = 0
    for w in words:
        if w == word:
            count += 1
    return count