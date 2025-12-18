"""
QUESTION:
Create a function called `consecutive_string` that takes two strings as input and returns whether the first string contains the second string consecutively and the total count of such occurrences. The comparison should be case-insensitive and only consider alphanumeric characters.
"""

import re

def consecutive_string(first_string, second_string):
    first_string = re.sub(r'\W', '', first_string.lower())
    second_string = re.sub(r'\W', '', second_string.lower())
    count = 0
    i = 0
    while i < len(first_string):
        if first_string[i:i+len(second_string)] == second_string:
            count += 1
            i += len(second_string)
        else:
            i += 1
    return count > 0, count