"""
QUESTION:
Write a function `is_permutation(str1, str2)` that checks if string `str1` is a permutation of string `str2`, considering only alphabetic characters and ignoring case. The function should handle strings of different lengths and strings containing special characters and spaces, have a time complexity of O(n log n), and use only constant extra space.
"""

def is_permutation(str1, str2):
    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Remove non-alphabetic characters
    str1 = ''.join(c for c in str1 if c.isalpha())
    str2 = ''.join(c for c in str2 if c.isalpha())

    # Check if the lengths are different
    if len(str1) != len(str2):
        return False

    # Sort the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Compare the sorted strings
    return sorted_str1 == sorted_str2