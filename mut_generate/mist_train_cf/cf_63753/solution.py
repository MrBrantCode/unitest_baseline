"""
QUESTION:
Create a function named `find_anagrams` that takes a list of words as input and returns a list of lists, where each sublist contains all the anagrams from the input list. The function should group the input words into anagrams and exclude any groups with less than two words.
"""

from collections import defaultdict

def find_anagrams(words):
    sorted_word_dict = defaultdict(list)
    for word in words:
        sorted_word_dict[''.join(sorted(word))].append(word)
    return [words for words in sorted_word_dict.values() if len(words) > 1]