"""
QUESTION:
Define a function `get_anagrams` that takes a string `s` as input and returns a sorted list of unique anagrams. The function should use recursion to generate all possible permutations of the input string, filter out duplicates, and return the result in ascending order. Assume that the input string contains only lowercase English letters and has a length of at least 1. The function should not use any external libraries or data structures other than built-in Python data types.
"""

def get_anagrams(s):
    if len(s) == 1:
        return [s]
    else:
        unique_anagrams = set()
        for i, c in enumerate(s):
            remaining = s[:i] + s[i+1:]
            for a in get_anagrams(remaining):
                unique_anagrams.add(c + a)
        return sorted(list(unique_anagrams))