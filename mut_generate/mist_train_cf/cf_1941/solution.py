"""
QUESTION:
Implement a function `are_anagrams(str1, str2)` that checks if two input strings are anagrams of each other without using any built-in sorting or hashing functions or libraries. The function should also not use any auxiliary data structures and have a time complexity less than O(n^2), where n is the length of the longer string. Assume that the input strings only contain lowercase English letters.
"""

def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    char_count = [0] * 26

    for char in str1:
        char_count[ord(char) - ord('a')] += 1

    for char in str2:
        char_count[ord(char) - ord('a')] -= 1

    for count in char_count:
        if count != 0:
            return False

    return True