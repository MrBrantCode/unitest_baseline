"""
QUESTION:
Write a function `validate_strings(s1, s2)` that takes two strings `s1` and `s2` as input and returns `True` if both strings pass the following conditions, and `False` otherwise:
 
Both strings should be at least 8 characters long and their combined length should not exceed 20 characters. 
`s1` should contain at least two special characters and at least one lowercase letter, and its first character should be a letter (uppercase or lowercase). 
`s2` should contain at least two uppercase letters, at least one numeric digit, and its last character should be a letter (uppercase or lowercase). 
Neither string should contain any consecutive repeating characters, and both strings should contain at least one whitespace character.
"""

def validate_strings(s1, s2):
    # Condition 1
    if len(s1) < 8 or len(s2) < 8 or len(s1) + len(s2) > 20:
        return False
    
    # Condition 2
    special_char_count = sum(1 for char in s1 if not char.isalnum())
    if special_char_count < 2 or not any(char.islower() for char in s1) or not s1[0].isalpha():
        return False
    
    # Condition 3
    uppercase_count = sum(1 for char in s2 if char.isupper())
    if uppercase_count < 2 or not any(char.isdigit() for char in s2) or not s2[-1].isalpha():
        return False
    
    # Condition 4
    if any(s1[i] == s1[i+1] for i in range(len(s1)-1)) or any(s2[i] == s2[i+1] for i in range(len(s2)-1)):
        return False
    
    # Condition 5
    if not any(char.isspace() for char in s1) or not any(char.isspace() for char in s2):
        return False
    
    return True