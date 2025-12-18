"""
QUESTION:
Create a function called `check_anagram` that takes two string parameters and returns a boolean value indicating whether the two strings are anagrams of each other. The function should not use any pre-defined string or sorting functions native to Python. Two strings are considered anagrams if they contain the same characters, but in different order, and are case-insensitive. Spaces in the strings should be ignored.
"""

def check_anagram(s1, s2):
    # Remove space and convert to lowercase
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Check if both strings have the same length
    if len(s1) != len(s2):
        return False

    # Create two dictionaries to save the characters and their frequency
    dict1 = {}
    dict2 = {}

    # Count the frequency of each character in the first string
    for char in s1:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1

    # Count the frequency of each character in the second string
    for char in s2:
        if char in dict2:
            dict2[char] += 1
        else:
            dict2[char] = 1

    # Compare the two dictionaries
    for key in dict1:
        if key not in dict2 or dict1[key] != dict2[key]:
            return False

    return True