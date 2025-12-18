"""
QUESTION:
Define a function `get_anagrams` that takes a string `s` as input and returns a sorted list of unique anagrams from the string, without any duplicates or non-anagrams. The input string may contain duplicate characters. The function should use recursion to generate all possible permutations of the input string and filter out duplicates and non-anagrams. The output list should be in ascending order.
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