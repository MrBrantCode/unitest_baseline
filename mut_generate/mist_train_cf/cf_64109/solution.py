"""
QUESTION:
Write a function `find_anagrams(word_list)` that takes an unordered list of words as input and returns groups of words that are anagrams of each other. If there are no groups of anagrams, the function should return "No anagrams found". The function should have a time complexity efficient enough to handle large lists of words.
"""

from collections import defaultdict

def find_anagrams(word_list):
    ana_dict = defaultdict(list)
    for word in word_list:
        ana_dict[''.join(sorted(word))].append(word)
    anagram_groups = [words for words in ana_dict.values() if len(words) > 1]
    if not anagram_groups:
        return "No anagrams found"
    return anagram_groups