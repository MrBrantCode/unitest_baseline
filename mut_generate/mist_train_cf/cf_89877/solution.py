"""
QUESTION:
Develop a function `are_anagrams(str1, str2)` that determines whether two input strings are anagrams. The function should not use built-in Python functions or libraries for string manipulation and sorting, and should have a time complexity of O(n) where n is the length of the strings. The function should also have a space complexity of O(1), meaning it should not use any additional data structures besides the input strings. Assume that the input strings only contain lowercase letters and no special characters or spaces.
"""

def entrance(str1, str2):
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