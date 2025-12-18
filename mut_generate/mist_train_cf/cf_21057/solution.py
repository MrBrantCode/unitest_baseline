"""
QUESTION:
Write a function named `is_anagram` that takes two strings as input and returns a boolean value indicating whether the strings are anagrams. The function must be case-insensitive and should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the longer string.
"""

def is_anagram(str1, str2):
    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Create a dictionary to count the occurrences of each character
    char_count = {}

    # Count the occurrences of each character in str1
    for char in str1:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1

    # Check if the characters in str2 match the counts in char_count
    for char in str2:
        if char.isalpha():
            if char not in char_count:
                return False
            char_count[char] -= 1

    # Check if any character count is not zero
    for count in char_count.values():
        if count != 0:
            return False

    # If all checks pass, the strings are anagrams
    return True