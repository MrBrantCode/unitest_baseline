"""
QUESTION:
Write a function `is_anagram(s1, s2)` that determines if `s1` is an anagram of `s2`. The function should ignore case sensitivity, consider only alphabetic characters, and have a space complexity of O(1). It should not use any built-in sorting or comparison functions and be able to handle strings with up to 10^6 characters within a 2-second time limit.
"""

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    s1 = ''.join(c for c in s1 if c.isalpha())
    s2 = ''.join(c for c in s2 if c.isalpha())

    if len(s1) != len(s2):
        return False

    count1 = [0] * 26
    count2 = [0] * 26

    for char in s1:
        count1[ord(char) - ord('a')] += 1

    for char in s2:
        count2[ord(char) - ord('a')] += 1

    return count1 == count2