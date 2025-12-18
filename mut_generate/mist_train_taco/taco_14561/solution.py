"""
QUESTION:
Given a hash of letters and the number of times they occur, recreate all of the possible anagram combinations that could be created using all of the letters, sorted alphabetically.

The inputs will never include numbers, spaces or any special characters, only lowercase letters a-z.

E.g. get_words({2=>["a"], 1=>["b", "c"]}) => ["aabc", "aacb", "abac", "abca", "acab", "acba", "baac", "baca", "bcaa", "caab", "caba", "cbaa"]
"""

from itertools import permutations

def generate_anagrams(letter_counts):
    # Flatten the dictionary into a single string of characters
    word = ''.join((qty * char for qty in letter_counts for chars in letter_counts[qty] for char in chars))
    
    # Generate all unique permutations of the word
    unique_permutations = {''.join(permutation) for permutation in permutations(word)}
    
    # Sort the permutations alphabetically
    return sorted(unique_permutations)