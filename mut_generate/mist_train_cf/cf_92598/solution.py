"""
QUESTION:
Create a function `check_anagram(str1, str2)` that takes two strings as arguments and returns True if the two strings contain the same characters, regardless of their order. The function should be case-insensitive, ignore any whitespace characters, and handle special characters and symbols.
"""

def check_anagram(str1, str2):
    # Removing whitespace characters and converting to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Sorting the strings alphabetically
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Checking if the sorted strings are equal
    return sorted_str1 == sorted_str2