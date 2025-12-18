"""
QUESTION:
Create a function `freq_dict_with_adjacent_pairs` that takes a list of strings as input and returns a dictionary containing the frequency of each unique word and pair of adjacent words, along with the total count of all words in the list.
"""

from collections import Counter

def freq_dict_with_adjacent_pairs(words):
    word_count = Counter(words)
    pairs = [words[i] + " " + words[i+1] for i in range(len(words)-1)]
    pair_count = Counter(pairs)
    all_counts = word_count + pair_count
    total_count = sum(all_counts.values())
    all_counts['total_count'] = total_count
    return all_counts