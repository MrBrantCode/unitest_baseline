"""
QUESTION:
Develop a function named `count_lower(s)` that takes a string `s` as input and returns the number of lowercase consonants found exclusively in odd indices. The function should consider 'a', 'e', 'i', 'o', 'u' as vowels and exclude them from the count.
"""

def count_lower(s):
    count = 0
    for i in range(len(s)):
        if i % 2 != 0 and s[i].islower() and s[i] not in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count