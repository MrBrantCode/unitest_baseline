"""
QUESTION:
Create a function `sort_string(s)` that takes a string `s` as input and returns a new string with the characters rearranged in alphabetical order, while keeping uppercase and lowercase characters separate. The function should process only alphabetic characters and ignore any other characters.
"""

def sort_string(s):
    upper_case = []
    lower_case = []
    for char in s:
        if char.isupper():
            upper_case.append(char)
        elif char.islower():
            lower_case.append(char)

    return ''.join(sorted(upper_case) + sorted(lower_case))