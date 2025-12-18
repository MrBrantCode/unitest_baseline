"""
QUESTION:
Write a function called `reverse_string` that takes a string as input, ignores any leading or trailing whitespace characters, treats uppercase and lowercase characters as equal, and returns the reversed string. The function should not use any built-in string manipulation functions or libraries, and should only use basic string operations and loops.
"""

def reverse_string(string):
    # Remove leading and trailing whitespace
    string = string.strip()

    # Convert the string to lowercase
    string = string.lower()

    # Reverse the string using a loop
    reversed_string = ''
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]

    return reversed_string