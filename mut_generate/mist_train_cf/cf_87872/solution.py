"""
QUESTION:
Write a function `longest_string_with_conditions(strings)` that takes a list of strings as input and returns the longest string that contains at least one uppercase letter, one lowercase letter, one special character (non-alphanumeric), and one digit. The function should have a time complexity of O(n), where n is the total number of characters in all strings combined, and a space complexity of O(1).
"""

def longest_string_with_conditions(strings):
    longest_string = ""
    for string in strings:
        has_uppercase = False
        has_lowercase = False
        has_special_character = False
        has_digit = False
        for char in string:
            if char.isupper():
                has_uppercase = True
            elif char.islower():
                has_lowercase = True
            elif not char.isalnum():
                has_special_character = True
            elif char.isdigit():
                has_digit = True
            if has_uppercase and has_lowercase and has_special_character and has_digit:
                if len(string) > len(longest_string):
                    longest_string = string
                break
    return longest_string