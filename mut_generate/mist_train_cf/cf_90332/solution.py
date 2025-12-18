"""
QUESTION:
Create a function `find_unique_strings(input_list: List[str]) -> List[str]` that returns a list of strings that occur exactly once in the given list. The function should exclude any strings that occur more than once in the input list.
"""

from typing import List

def find_unique_strings(input_list: List[str]) -> List[str]:
    counts = {}
    
    # Count the occurrences of each string in the input list
    for string in input_list:
        if string in counts:
            counts[string] += 1
        else:
            counts[string] = 1
    
    # Return the strings that occur exactly once
    return [string for string in input_list if counts[string] == 1]