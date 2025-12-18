"""
QUESTION:
Write a function `find_first_non_duplicate(s)` to find the first non-duplicate character in a given string `s`. The function should be case-insensitive, treating both uppercase and lowercase letters as the same, and also consider special characters and numbers in the string. The function should return the first non-duplicate character in the string. If no non-duplicate character is found, the function should return `None`.
"""

def find_first_non_duplicate(s):
    s = s.lower()
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in s:
        if freq[char] == 1:
            return char
    return None