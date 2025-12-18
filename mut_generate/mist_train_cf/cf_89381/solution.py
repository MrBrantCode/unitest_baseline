"""
QUESTION:
Write a function `count_substring_occurrences(s1, s2)` that takes two strings `s1` and `s2` as input and returns the number of non-overlapping substrings of `s2` with a length of at least 3 that appear in `s1`. The matching should be case-sensitive and the function should count each occurrence separately.
"""

def count_substring_occurrences(s1, s2):
    counter = 0
    left = 0
    right = 0
    counted_substrings = set()
    
    while right < len(s1):
        substring = s1[left:right+1]
        
        if len(substring) >= 3 and substring in s2:
            if substring not in counted_substrings:
                counter += 1
                counted_substrings.add(substring)
        
        if right - left + 1 >= len(s2):
            left += 1
        
        right += 1
    
    return counter