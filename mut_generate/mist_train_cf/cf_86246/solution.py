"""
QUESTION:
Write a function `is_anagram(str1, str2)` that checks whether two input strings are anagrams of each other. The function should trim any leading or trailing whitespace from the input strings, consider all characters (including uppercase and lowercase letters, numbers, and special characters), be case-insensitive, and have a time complexity of O(n), where n is the length of the longest string. The function should return False if either string has a length of less than 2 characters or if the strings are not anagrams; otherwise, it should return True.
"""

def entrance(str1, str2):
    # Trim whitespace and convert to lowercase
    str1 = str1.strip().lower()
    str2 = str2.strip().lower()

    # Check if strings are empty or have length less than 2
    if len(str1) < 2 or len(str2) < 2:
        return False

    # Create frequency dictionaries for characters in both strings
    freq1 = {}
    freq2 = {}

    for char in str1:
        freq1[char] = freq1.get(char, 0) + 1

    for char in str2:
        freq2[char] = freq2.get(char, 0) + 1

    # Compare the frequency dictionaries
    return freq1 == freq2