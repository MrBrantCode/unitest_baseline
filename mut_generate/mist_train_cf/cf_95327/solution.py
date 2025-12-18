"""
QUESTION:
Write a function `is_permutation(str1, str2)` that checks if `str1` is a permutation of `str2` considering only alphabetic characters and ignoring case. The function should handle strings with different lengths and strings containing special characters and spaces. The time complexity should be O(n) where n is the length of the longer string.
"""

def is_permutation(str1, str2):
    # Remove non-alphabetic characters and convert to lowercase
    str1 = ''.join(filter(str.isalpha, str1.lower()))
    str2 = ''.join(filter(str.isalpha, str2.lower()))

    # Check if lengths are different
    if len(str1) != len(str2):
        return False

    # Count the occurrence of each character in str1
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Decrement the count for each character in str2
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            # If a character in str2 is not present in str1, return False
            return False

    # Check if all counts are zero
    for count in char_count.values():
        if count != 0:
            return False

    return True