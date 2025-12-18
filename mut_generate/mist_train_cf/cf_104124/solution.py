"""
QUESTION:
Write a recursive function `reverse_print_string(s)` that takes a string `s` of uppercase letters with a length between 3 and 10 characters as input, and prints each letter of the string in reverse order.
"""

def entance(s):
    # Base case: if the length of the string is 0, return
    if len(s) == 0:
        return

    # Recursive case: print the last character of the string
    print(s[-1], end="")

    # Call the function recursively with the remaining substring
    entance(s[:-1])