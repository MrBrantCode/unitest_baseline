"""
QUESTION:
Create a function called `reverse_string` that takes a string `user_string` as input and returns the reversed string. The function should be case-insensitive, meaning the input string should be converted to either lowercase or uppercase before being reversed. The function should handle empty strings and not enter into an infinite recursion.
"""

def entrance(user_string):
    user_string = user_string.lower()
    if len(user_string) == 0:
        return ""
    else:
        return entrance(user_string[1:]) + user_string[0]