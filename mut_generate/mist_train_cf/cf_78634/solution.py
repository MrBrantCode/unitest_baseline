"""
QUESTION:
Find the anagram of a given target string within a list of strings. Write a function `find_anagram(words, target)` that takes a list of strings `words` and a target string `target`, and returns the first string in `words` that is an anagram of `target`. If no such string exists, return `None`. The comparison is case-sensitive.
"""

def find_anagram(words, target):
    sorted_target = sorted(target)
    
    for word in words:
        if sorted(word) == sorted_target:
            return word
    return None