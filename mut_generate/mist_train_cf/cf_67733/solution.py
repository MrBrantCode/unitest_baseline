"""
QUESTION:
Write a function `check_string(my_string)` that takes a string as input. The function should return the count of numeric characters in the string if the string contains only alpha-numeric characters and all alphabets are unique (case-sensitive). Otherwise, return `False`.
"""

def check_string(my_string):
    if my_string.isalnum():
        if len(my_string) == len(set(my_string)):
            return sum(c.isdigit() for c in my_string)
        else:
            return False
    else:
        return False