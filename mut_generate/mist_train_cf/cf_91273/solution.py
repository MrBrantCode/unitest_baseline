"""
QUESTION:
Write a function `are_anagrams(str1, str2)` that checks if two given strings are anagrams of each other. The function should return `True` if the strings are anagrams and `False` otherwise. The function should ignore case differences and whitespace characters. The implementation should not use any built-in sorting or hashing functions or libraries. The strings only contain letters of the English alphabet.
"""

def entance(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    count1 = [0] * 26
    count2 = [0] * 26

    for char in str1:
        index = ord(char) - ord('a')
        count1[index] += 1

    for char in str2:
        index = ord(char) - ord('a')
        count2[index] += 1

    for i in range(26):
        if count1[i] != count2[i]:
            return False

    return True