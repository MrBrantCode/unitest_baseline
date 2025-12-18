"""
QUESTION:
Implement a function called `is_unique` that takes a string of printable ASCII characters as input and returns `True` if all characters in the string are unique and `False` otherwise. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string. You cannot use additional data structures, built-in functions or libraries that directly solve the problem, sorting algorithms, or modify the input string. The function should also handle uppercase and lowercase letters as different characters and cannot convert the input string to lowercase or uppercase.
"""

def is_unique(s):
    if len(s) > 128:
        return False
    
    char_set = [False] * 128
    
    for char in s:
        ascii_value = ord(char)
        
        if char_set[ascii_value]:
            return False
        
        char_set[ascii_value] = True
    
    return True