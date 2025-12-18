"""
QUESTION:
Write a function `is_permutation(str1, str2)` that checks if string `str1` is a permutation of string `str2`. The function should be case-sensitive, handle strings with different lengths, special characters, and spaces. It should return `True` if `str1` is a permutation of `str2`, and `False` otherwise, with a time complexity of O(n), where n is the length of the longer string.
"""

def is_permutation(str1, str2):
    # Check if the lengths of the strings are different
    if len(str1) != len(str2):
        return False
    
    # Create a dictionary to store the frequency of characters in str1
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Iterate through str2 and decrement the frequency of characters in char_count
    # If a character is not found in char_count or its frequency becomes negative, return False
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        else:
            return False
    
    # Check if all the frequencies in char_count are zero
    for freq in char_count.values():
        if freq != 0:
            return False
    
    # If all checks pass, return True
    return True