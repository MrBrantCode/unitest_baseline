"""
QUESTION:
Create a function called `are_anagrams` that takes two parameters, `str1` and `str2`, and checks if the two strings are anagrams of each other. The function should not use any built-in sorting or hashing functions, and it should not use any auxiliary data structures. The function should return a boolean value indicating whether the two strings are anagrams or not. The time complexity of the function should be less than O(n^2), where n is the length of the longer string. Assume that the input strings only contain lowercase letters.
"""

def entance(str1, str2):
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