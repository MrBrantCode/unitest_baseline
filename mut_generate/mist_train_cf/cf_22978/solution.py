"""
QUESTION:
Create a function `has_unique_chars_and_substrings` that takes a string of lowercase alphabets as input and returns True if the string has all unique characters and no duplicate substrings of length greater than 3, and False otherwise. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string.
"""

def has_unique_chars_and_substrings(string):
    if len(string) > 26:
        return False
    char_set = [False] * 26
    for char in string:
        if char_set[ord(char) - ord('a')]:
            return False
        char_set[ord(char) - ord('a')] = True
    for i in range(len(string) - 3):
        for j in range(i + 1, len(string) - 2):
            if string[i:i+3] == string[j:j+3]:
                return False
    return True