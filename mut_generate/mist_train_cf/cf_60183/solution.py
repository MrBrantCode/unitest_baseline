"""
QUESTION:
Create a function `manipulate_strings` that takes a list of strings as input. The function should reverse each string in the list, capitalize the first and last character of each string, and handle edge cases where a string is empty or contains only one character.
"""

def manipulate_strings(input_list):
    result = []
    for s in input_list:
        if len(s) > 1:
            result.append(s[-1].upper() + s[1:-1][::-1] + s[0].upper())
        elif s:
            result.append(s.upper())
        else:
            result.append(s)
    return result