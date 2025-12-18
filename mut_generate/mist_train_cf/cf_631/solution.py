"""
QUESTION:
Write a function `are_anagrams(str1, str2)` that checks if two strings are anagrams. The function should be case-insensitive, ignore non-alphabetic characters, and have a time complexity of O(n) and a space complexity of O(1). The function should not use built-in string manipulation or sorting functions.
"""

def are_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False

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