"""
QUESTION:
Create a function `common_substrings(s1, s2)` that takes two strings `s1` and `s2` as input and returns the number of common substrings between them. In this context, substrings are contiguous sequences of characters within a string. The function should count each common substring as many times as it appears in both strings, but no more than the minimum frequency of the substring in either string.
"""

def common_substrings(s1, s2):
    # Initialize counters for each string's substrings
    substrings_s1 = {}
    substrings_s2 = {}
  
    # Get all substrings of s1
    for i in range(len(s1)):
        for j in range(i + 1, len(s1) + 1):
            substring = s1[i:j]
            if substring not in substrings_s1:
                substrings_s1[substring] = 1
            else:
                substrings_s1[substring] += 1
            
    # Get all substrings of s2
    for i in range(len(s2)):
        for j in range(i + 1, len(s2) + 1):
            substring = s2[i:j]
            if substring not in substrings_s2:
                substrings_s2[substring] = 1
            else:
                substrings_s2[substring] += 1
    
    # Count common substrings
    common_count = 0
    for sub in substrings_s1:
        if sub in substrings_s2:
            common_count += min(substrings_s1[sub], substrings_s2[sub])
    
    return common_count