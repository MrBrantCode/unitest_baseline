"""
QUESTION:
Given two strings `word1` and `word2`, return the minimum number of steps required to make `word1` and `word2` the same by deleting characters that are vowels (a, e, i, o, u). If it is not possible to make the two strings the same using the given constraints, return -1. The function `minSteps(word1, word2)` should be implemented with the constraints that `1 <= word1.length, word2.length <= 500` and `word1` and `word2` consist of only lowercase English letters.
"""

def minSteps(word1, word2):
    vowels = 'aeiou'

    word1_consonant = ''.join([char for char in word1 if char not in vowels])
    word2_consonant = ''.join([char for char in word2 if char not in vowels])

    if word1_consonant != word2_consonant:
        return -1

    word1_vowel = [char for char in word1 if char in vowels]
    word2_vowel = [char for char in word2 if char in vowels]

    common_vowel = [char for char in word1_vowel if char in word2_vowel]

    return len(word1_vowel) + len(word2_vowel) - 2*len(common_vowel)