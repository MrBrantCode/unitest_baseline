"""
QUESTION:
Write a function `check_anagrams` that takes a list of tuples as input, where each tuple contains two strings that may contain special characters and vary in letter case. The function should return a list of tuples, where each tuple contains the original two strings and a boolean value indicating whether the strings are anagrams of each other, ignoring letter case and special characters. The function should handle each pair of strings in the input list independently.
"""

def check_anagrams(pairs):
    def are_anagrams(s1, s2):
        s1 = ''.join(e for e in s1 if e.isalnum()).lower()
        s2 = ''.join(e for e in s2 if e.isalnum()).lower()
        return sorted(s1) == sorted(s2)
    
    return [(s1, s2, are_anagrams(s1, s2)) for s1, s2 in pairs]