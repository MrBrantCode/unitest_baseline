"""
QUESTION:
Write a function named `is_anagram` that takes two strings as parameters and returns a boolean indicating whether they are anagrams of each other. The function should consider both uppercase and lowercase letters as equal and ignore whitespace. The function should have a time complexity of O(n log n) or better. If the strings have different lengths, the function should return False.
"""

def is_anagram(s1, s2):
    # Convert both strings to lowercase and remove whitespace
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")

    # Check if the lengths are equal
    if len(s1) != len(s2):
        return False

    # Convert the strings into lists of characters and sort them
    return sorted(s1) == sorted(s2)