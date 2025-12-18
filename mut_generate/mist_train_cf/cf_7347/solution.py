"""
QUESTION:
Write a function `are_anagrams` that takes two strings as input and returns `True` if they are anagrams and `False` otherwise, with the following restrictions:

- The function must have a time complexity of O(n), where n is the length of the strings.
- The function must have a space complexity of O(1), meaning it should not use any additional data structures besides the input strings.
- The input strings only contain lowercase letters and no special characters or spaces.
"""

def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    counter = [0] * 26

    for char in str1:
        index = ord(char) - ord('a')
        counter[index] += 1

    for char in str2:
        index = ord(char) - ord('a')
        counter[index] -= 1

    for count in counter:
        if count != 0:
            return False

    return True