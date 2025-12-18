"""
QUESTION:
Write a function named `is_anagram` that takes two string parameters, `str1` and `str2`, and returns a boolean indicating whether they are anagrams of each other. The function should ignore case, trim leading and trailing whitespace, and consider all characters. The function should return `False` if either string is empty or has a length less than 2. The time complexity of the function should be O(n), where n is the length of the longest string.
"""

def is_anagram(str1, str2):
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