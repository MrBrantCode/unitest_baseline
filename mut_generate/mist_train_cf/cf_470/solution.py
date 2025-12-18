"""
QUESTION:
Create a function `is_rotation` that determines whether two given strings are rotations of each other. The function should take two parameters: `string1` and `string2`, both consisting of lowercase alphabets and/or digits with lengths between 1 and 10^5 inclusive. The function should return True if `string1` and `string2` are rotations of each other, and False otherwise. The time complexity of the solution should be O(n), where n is the length of the longer string among `string1` and `string2`.
"""

def is_rotation(s1: str, s2: str) -> bool:
    # Check if the lengths of the strings are equal
    if len(s1) != len(s2):
        return False
    
    # Concatenate string1 with itself
    concatenated_string = s1 + s1
    
    # Check if string2 is a substring of the concatenated string
    return s2 in concatenated_string