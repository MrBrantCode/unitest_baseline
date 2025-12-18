"""
QUESTION:
Create a function `check_nearly_identical(str1, str2)` that checks whether two input strings `str1` and `str2` are nearly identical, considering that the order of characters in the strings is not important. The function should return `True` if the strings are nearly identical and `False` otherwise. The solution should have a time complexity of O(n), where n is the length of the input strings.
"""

def check_nearly_identical(str1, str2):
    if len(str1) != len(str2):
        return False
    
    char_count = {}
    
    # Count the occurrence of each character in str1
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Compare the occurrence of each character in str2
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
        else:
            return False
    
    return len(char_count) == 0