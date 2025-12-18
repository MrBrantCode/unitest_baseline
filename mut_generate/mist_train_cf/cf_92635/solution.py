"""
QUESTION:
Write a function called `is_anagram` that takes two strings as input and returns a boolean indicating whether the strings are anagrams of each other. The function should have a time complexity of O(n log n) and a space complexity of O(1), where n is the length of the input strings.
"""

def is_anagram(str1, str2):
    # Convert both strings to lowercase and remove whitespace
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    # Check if the lengths of the strings are different
    if len(str1) != len(str2):
        return False

    # Sort both strings and compare them
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    return sorted_str1 == sorted_str2