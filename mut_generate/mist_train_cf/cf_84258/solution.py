"""
QUESTION:
Given two strings, ransomNote and magazine, both containing only lowercase letters, write a function canConstruct(ransomNote, magazine) that returns a tuple containing a boolean indicating whether the ransom note can be constructed from the magazines, and the minimum number of magazines needed to construct the ransom note if it can be constructed. Each letter in the magazine string can only be used once in the ransom note. The function should assume that the length of both strings will not exceed 10^5.
"""

def canConstruct(ransomNote, magazine):
    freq_magazine = {}
    for letter in magazine:
        if letter in freq_magazine:
            freq_magazine[letter] += 1
        else:
            freq_magazine[letter] = 1

    min_magazines = 0
    for letter in ransomNote:
        if letter in freq_magazine and freq_magazine[letter] > 0:
            freq_magazine[letter] -= 1
            if freq_magazine[letter] == 0:
                min_magazines += 1
        else:
            return False, 0

    return True, min_magazines