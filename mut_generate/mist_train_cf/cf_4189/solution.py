"""
QUESTION:
Create a function `compare_strings` that takes two strings `string1` and `string2` as arguments. The function should return `True` if the strings are equal and `False` otherwise, with the following restrictions: 
- the comparison is case-sensitive 
- the strings do not contain any leading or trailing whitespace characters 
- the strings do not exceed a length of 100 characters 
- the strings can only contain alphanumeric characters and special characters (!@#$%^&*().
"""

def entance(string1, string2):
    string1 = string1.strip()
    string2 = string2.strip()

    if not string1 and not string2:
        return True

    if len(string1) > 100 or len(string2) > 100:
        return False

    if not all(char.isalnum() or char in '!@#$%^&*()' for char in string1) or not all(char.isalnum() or char in '!@#$%^&*()' for char in string2):
        return False

    return string1 == string2