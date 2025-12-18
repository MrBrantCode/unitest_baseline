"""
QUESTION:
Write a function named `count_vowels` that takes a string `word` as input and returns a dictionary with each vowel in the word as the key and its corresponding frequency in the word as the value. The function should only include vowels that appear at least once in the word.
"""

def entrance(word):
    return {v: word.count(v) for v in 'aeiou' if word.count(v) > 0}