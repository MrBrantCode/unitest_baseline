"""
QUESTION:
Write a function called `reverse_full_name` that takes a first name and a last name as input, reverses both names, and combines them into a single string with a space in between. The resulting full name should be returned as the function's output.
"""

def reverse_full_name(first_name, last_name):
    return last_name[::-1] + ' ' + first_name[::-1]