"""
QUESTION:
Write a function named `find_anagram_pairs` that takes a list of strings as input and returns a list of tuples containing all pairs of anagrams. The function should be efficient enough to handle large lists of strings with varying lengths.
"""

from collections import defaultdict
def find_anagram_pairs(strings):
    # Create a dictionary to store the sorted strings as keys and their original strings as values
    sorted_strings = defaultdict(list)
    for s in strings:
        sorted_strings[''.join(sorted(s))].append(s)
    
    # Find all pairs of anagrams
    anagram_pairs = []
    for key in sorted_strings:
        if len(sorted_strings[key]) > 1:
            for i in range(len(sorted_strings[key])):
                for j in range(i+1, len(sorted_strings[key])):
                    anagram_pairs.append((sorted_strings[key][i], sorted_strings[key][j]))
    
    return anagram_pairs