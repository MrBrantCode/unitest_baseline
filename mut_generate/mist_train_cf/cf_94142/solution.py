"""
QUESTION:
Create a function called `contains_uv_consecutively` that takes a string as input and returns a boolean. The function should check if the string contains the letter "u" followed by the letter "v" consecutively, excluding any occurrences of "uv" that are immediately preceded by "u". The function should return True if such a sequence is found, and False otherwise.
"""

def contains_uv_consecutively(string):
    for i in range(len(string)-1):
        if string[i] == 'u' and string[i+1] == 'v' and (i == 0 or string[i-1] != 'u'):
            return True
    return False