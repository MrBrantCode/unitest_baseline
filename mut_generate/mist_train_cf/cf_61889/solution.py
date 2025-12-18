"""
QUESTION:
Write a function `sum_ord_lower(s)` that takes a string `s` as input and returns the sum of the ASCII values of all lower-case non-vowel characters at odd positions in the reversed string. A position is considered odd if its index is even (0-based indexing). Non-vowel characters are all lower-case letters except 'a', 'e', 'i', 'o', and 'u'.
"""

def sum_ord_lower(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    total = 0
    s = s[::-1]  # reverse the string
    
    # iterate over odd characters only
    for i in range(len(s)):
        if i % 2 == 0 and s[i].islower() and s[i] not in vowels:
            total += ord(s[i])
            
    return total