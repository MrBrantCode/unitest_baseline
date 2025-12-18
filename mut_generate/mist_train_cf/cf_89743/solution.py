"""
QUESTION:
Write a function `unique_chars(s1, s2)` that takes two strings `s1` and `s2` as input. The function should return a new string containing the alphabetic characters present only in `s1`, ignoring case sensitivity and duplicates, and sorted in ascending order. The strings may contain special characters, numbers, or spaces, but those should not be considered in the result. The length of `s1` and `s2` will be at most 10^5.
"""

def unique_chars(s1, s2):
    uniqueChars = set()
    s1 = s1.lower()
    s2 = s2.lower()
    
    for c in s1:
        if c.isalpha():
            uniqueChars.add(c)
    
    for c in s2:
        if c.isalpha() and c in uniqueChars:
            uniqueChars.remove(c)
    
    sortedChars = sorted(list(uniqueChars))
    return ''.join(sortedChars)