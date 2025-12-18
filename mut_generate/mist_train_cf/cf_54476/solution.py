"""
QUESTION:
Implement a function `check_anagram(s1, s2)` that checks if two given strings are case-sensitive anagrams of each other, ignoring punctuation and white spaces, without using built-in library functions or data structures, including arrays. The function should return a boolean value indicating whether the strings are anagrams.
"""

def check_anagram(s1, s2):
    s1 = ''.join(filter(str.isalpha, s1)).lower()
    s2 = ''.join(filter(str.isalpha, s2)).lower()
    hist1 = ''
    hist2 = ''
    
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        count1 = 0
        count2 = 0
        for sub in s1:
            if sub == ch:
                count1 += 1
        for sub in s2:
            if sub == ch:
                count2 += 1
        hist1 += str(count1)
        hist2 += str(count2)
    
    return hist1 == hist2