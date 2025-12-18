"""
QUESTION:
Create a function called `find_all_positions` that takes three parameters: `input_string`, `substring`, and `case_insensitive` (optional, default is `False`). The function should return a list of positions where the `substring` appears in the `input_string`. If `case_insensitive` is `True`, the function should perform a case-insensitive search. The function should not use any built-in string search functions or external libraries.
"""

def find_all_positions(input_string, substring, case_insensitive=False):
    positions = []
    
    if case_insensitive:
        input_string = input_string.lower()
        substring = substring.lower()

    index = 0
    while index < len(input_string):
        if input_string[index:index+len(substring)] == substring:
            positions.append(index)
        index += 1
    return positions