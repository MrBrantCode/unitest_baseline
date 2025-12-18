"""
QUESTION:
Create a function named `print_string_multiple_times` that takes two parameters: a string with a minimum length of 5 characters and an integer between 1 and 10 (inclusive). The function should print the string the given number of times.
"""

def entrance(s, n):
    if len(s) < 5:
        print("The string must contain at least 5 characters.")
        return
    if n < 1 or n > 10:
        print("The integer must be within the range of 1 to 10.")
        return
    for i in range(n):
        print(s)