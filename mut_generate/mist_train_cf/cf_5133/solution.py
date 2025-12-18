"""
QUESTION:
Create a function `check_conditions(string)` that takes a string of length 10 as input and returns True if it meets the following conditions and False otherwise:

- The string consists of characters 'a' to 'e'.
- The string contains at least two occurrences of the character 'a'.
- The string contains exactly one occurrence of the character 'b'.
- The character 'c' appears before the character 'd'.
- The characters 'b' and 'd' are not adjacent to each other in the string.
"""

def check_conditions(string):
    if string.count('a') < 2:
        return False
    if string.count('b') != 1:
        return False
    if string.count('c') == 0 or string.count('d') == 0:
        return False
    if 'bd' in string or 'db' in string:
        return False
    if string.index('c') > string.index('d'):
        return False
    for char in string:
        if char not in 'abcde':
            return False
    return True