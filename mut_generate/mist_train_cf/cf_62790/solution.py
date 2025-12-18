"""
QUESTION:
Create a function `find_substring(s, sub)` that finds all occurrences of a substring `sub` within a string `s`, including overlapping sequences, and returns their starting and ending positions. The function should take two parameters: `s` (the main string) and `sub` (the substring to search for).
"""

def find_substring(s, sub):
    start = 0
    while start < len(s):
        start = s.find(sub, start)
        if start == -1: 
            return
        yield (start, start + len(sub))
        start += 1