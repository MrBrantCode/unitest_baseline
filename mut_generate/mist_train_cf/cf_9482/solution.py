"""
QUESTION:
Create a recursive function named `print_reverse` that takes a string as an argument and prints each letter of the string in reverse order. The function should not return any value.
"""

def print_reverse(string):
    if len(string) == 0:
        return
    else:
        print_reverse(string[1:])
        print(string[0])