"""
QUESTION:
Write a function named `count_substring_occurrences(s1, s2)` that takes two strings `s1` and `s2` as input and returns the number of times a substring of `s2` with length greater than or equal to 2 appears in `s1`. The function should consider the following constraints: 

- Both strings can contain uppercase and lowercase letters.
- The characters in both strings can be in any order.
- The characters in `s2` can be repeated multiple times, and each occurrence should be counted separately.
- The matching should be case-sensitive.
- The characters in both strings can be any printable ASCII characters.
"""

def count_substring_occurrences(s1, s2):
    count = 0
    for i in range(2, len(s2)+1):
        for j in range(len(s2)-i+1):
            sub = s2[j:j+i]
            if sub in s1:
                count += 1
    return count