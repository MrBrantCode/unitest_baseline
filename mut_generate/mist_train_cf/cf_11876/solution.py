"""
QUESTION:
Write a recursive function named `reverse_print` that takes a string as input, reverses it, and then prints the reversed string. The function should not return any value, instead, it should directly print the result.
"""

def reverse_print(string):
    if len(string) == 0:
        return
    reverse_print(string[1:])
    print(string[0], end='')