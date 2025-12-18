"""
QUESTION:
Write a function `find_smallest_rep_unit(s)` that takes a string `s` as input and returns the smallest repeating unit of the string along with the number of times it is repeated. If no repeating unit is found, return 'None'. The function should also handle non-string inputs and return "Invalid input. Please input a string." in such cases. The input string `s` can be empty.
"""

def find_smallest_rep_unit(s):
    if not isinstance(s, str):
        return "Invalid input. Please input a string."
    
    if len(s) == 0:
        return "Invalid input. Please input a non-empty string."
    
    for rep_unit_size in range(1, len(s) // 2 + 1):
        rep_unit = s[:rep_unit_size]
        
        if len(s) % rep_unit_size == 0:
            full_rep_unit = rep_unit * (len(s) // rep_unit_size)
            
            if full_rep_unit == s:
                return rep_unit, len(s) // rep_unit_size
    
    return 'None'