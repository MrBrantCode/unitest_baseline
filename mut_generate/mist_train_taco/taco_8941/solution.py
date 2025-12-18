"""
QUESTION:
An anagram is a word, a phrase, or a sentence formed from another by rearranging its letters. An example of this is "angel", which is an anagram of "glean".

Write a function that receives an array of words, and returns the total number of distinct pairs of anagramic words inside it.

Some examples:

- There are 2 anagrams in the array `["dell", "ledl", "abc", "cba"]`
- There are 7 anagrams in the array `["dell", "ledl", "abc", "cba", "bca", "bac"]`
"""

from collections import Counter

def count_anagram_pairs(words):
    # Create a Counter object to count occurrences of each sorted word
    anagram_counts = Counter(''.join(sorted(word)) for word in words)
    
    # Calculate the number of anagram pairs for each unique sorted word
    # The formula n * (n - 1) // 2 gives the number of pairs for n occurrences
    return sum((n * (n - 1) // 2 for n in anagram_counts.values()))