"""
QUESTION:
Write a function `longest_valid_string` that takes a list of strings as input and returns the longest string that contains at least one uppercase letter, one lowercase letter, and one special character (non-alphanumeric). The function should have a time complexity of O(n), where n is the total number of characters in all strings combined, and a space complexity of O(1).
"""

def longest_valid_string(strings):
    def has_uppercase(s):
        return any(c.isupper() for c in s)

    def has_lowercase(s):
        return any(c.islower() for c in s)

    def has_special(s):
        return any(not c.isalnum() for c in s)

    longest_string = ""
    for string in strings:
        if (has_uppercase(string) and has_lowercase(string) and 
            has_special(string) and len(string) > len(longest_string)):
            longest_string = string
    return longest_string