"""
QUESTION:
Write a function named `check_strings` that takes an array of strings as input and returns a boolean. The function should return True if all strings in the array contain at least three digits, three lowercase letters, and three special characters. It should return False otherwise.
"""

def check_strings(arr):
    for string in arr:
        digit_count = 0
        lowercase_count = 0
        special_char_count = 0
        
        for char in string:
            if char.isdigit():
                digit_count += 1
            elif char.islower():
                lowercase_count += 1
            elif not char.isalnum():
                special_char_count += 1
        
        if digit_count < 3 or lowercase_count < 3 or special_char_count < 3:
            return False
    
    return True