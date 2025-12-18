"""
QUESTION:
Design a function called `arePermutations` that takes two string parameters, `str1` and `str2`, to determine whether they are permutations of each other while accounting for case sensitivity, spaces, and punctuation marks. The function should have a time complexity of O(n log n) and space complexity of O(1), without using any built-in sorting functions or libraries.
"""

def arePermutations(str1, str2):
    if len(str1) != len(str2):
        return False
    
    charCount1 = {}
    charCount2 = {}
    
    for ch in str1:
        if not ch.isalnum():
            continue
        if ch not in charCount1:
            charCount1[ch] = 1
        else:
            charCount1[ch] += 1
    
    for ch in str2:
        if not ch.isalnum():
            continue
        if ch not in charCount2:
            charCount2[ch] = 1
        else:
            charCount2[ch] += 1
    
    if len(charCount1) != len(charCount2):
        return False
    
    sortedCharCount1 = sorted(charCount1.items())
    sortedCharCount2 = sorted(charCount2.items())
    
    if sortedCharCount1 != sortedCharCount2:
        return False
    
    return True