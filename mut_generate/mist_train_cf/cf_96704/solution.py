"""
QUESTION:
Create a function named `check_nearly_identical` that takes two strings `str1` and `str2` as input and returns a boolean value indicating whether the two strings are nearly identical, considering the order of characters as unimportant. The function should have a time complexity of O(n), where n is the length of the input strings.
"""

def check_nearly_identical(str1, str2):
    if len(str1) != len(str2):
        return False
    
    char_count = {}
    
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
        else:
            return False
    
    return len(char_count) == 0