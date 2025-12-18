"""
QUESTION:
Write a function named `are_anagrams` that takes two strings `str1` and `str2` as input and returns `True` if they are anagrams, `False` otherwise. The function should be case-insensitive, ignore non-alphabetic characters, and have a time complexity of O(n) and a space complexity of O(1), where n is the total number of characters in both strings. The function should not use any built-in string manipulation or sorting functions.
"""

def are_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    count = [0] * 26

    for char in str1:
        if 'a' <= char <= 'z':
            count[ord(char) - ord('a')] += 1

    for char in str2:
        if 'a' <= char <= 'z':
            count[ord(char) - ord('a')] -= 1

    for i in range(26):
        if count[i] != 0:
            return False

    return True