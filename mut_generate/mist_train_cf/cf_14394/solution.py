"""
QUESTION:
Implement a function `validate_strings(s1, s2)` that takes two strings as input and returns True if both strings meet the following conditions, and False otherwise: 
1. The length of both strings should be at least 5 characters.
2. The combined length of both strings should not exceed 15 characters.
3. String `s1` should contain at least one special character.
4. String `s2` should contain at least one uppercase letter.
5. Both strings should not contain any consecutive repeating characters.
"""

def validate_strings(s1, s2):
    # Check length conditions
    if len(s1) < 5 or len(s2) < 5 or len(s1) + len(s2) > 15:
        return False
    
    # Check for special character in s1
    special_chars = '!@#$%^&*()_-+={}[]:;"\',.<>/?'
    if not any(char in special_chars for char in s1):
        return False
    
    # Check for uppercase letter in s2
    if not any(char.isupper() for char in s2):
        return False
    
    # Check for consecutive repeating characters in s1 and s2
    if any(char1 == char2 for char1, char2 in zip(s1, s1[1:])) or any(char1 == char2 for char1, char2 in zip(s2, s2[1:])):
        return False
    
    # All conditions passed
    return True