"""
QUESTION:
Create a function `solve_problem` that takes two parameters: `n` (the index after which the string will be sliced) and `s` (the string itself). The function should slice the string after the nth character, reverse the sliced string, and remove duplicates while ignoring case. If `n` is greater than the length of the string, return "Index out of range".
"""

def solve_problem(n, s):
    if n > len(s):
        return "Index out of range"
    else:
        sliced_string = s[n:]
        reversed_string = sliced_string[::-1]
        no_duplicate_string = ""
        for char in reversed_string:
            if char.lower() not in no_duplicate_string.lower():
                no_duplicate_string += char
        return no_duplicate_string