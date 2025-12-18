"""
QUESTION:
Write a function `is_anagram(string1, string2)` that takes two strings as parameters. The function should return `True` if the two strings are anagrams of each other, ignoring case and whitespace, and `False` otherwise. The function should also handle cases where the strings have different lengths and return `False` in such cases.
"""

def entrance(string1, string2):
    # Convert both strings to lowercase and remove whitespace
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")

    # Check if the lengths are equal
    if len(string1) != len(string2):
        return False

    # Sort both strings
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)

    # Compare the sorted strings
    if sorted_string1 == sorted_string2:
        return True
    else:
        return False