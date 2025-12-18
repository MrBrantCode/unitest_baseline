"""
QUESTION:
Create a function `word_anagram_frequency(word_list, target_word)` that takes a list of strings `word_list` and a string `target_word` as input. The function should be case-insensitive and return the frequency of the `target_word` in `word_list`, including the frequency of its anagrams.
"""

from collections import Counter

def word_anagram_frequency(word_list, target_word):
    target_word = target_word.lower()
    word_list = [word.lower() for word in word_list]

    def is_anagram(word1, word2):
        return Counter(word1) == Counter(word2)

    count = 0
    for word in word_list:
        if word == target_word or is_anagram(word, target_word):
            count += 1

    return count