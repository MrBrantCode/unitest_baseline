"""
QUESTION:
Write a function `check_conditions(string)` that takes a string as input and returns `True` if it meets the following conditions, and `False` otherwise: 
- The string has a length of 10. 
- The string is composed only of the characters 'a', 'b', 'c', 'd', and 'e'. 
- The string contains at least two occurrences of the character 'a'. 
- The string contains exactly one occurrence of the character 'b'. 
- The string contains at least one occurrence of both 'c' and 'd', and 'c' appears before 'd'. 
- The characters 'b' and 'd' are not adjacent to each other in the string.
"""

def check_conditions(string):
    if len(string) != 10:
        return False
    if not set(string).issubset('abcde'):
        return False
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
    return True