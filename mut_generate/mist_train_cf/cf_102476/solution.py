"""
QUESTION:
Create a function called `filter_and_sort_strings` that filters a list of strings based on their length and returns a new list with the filtered strings sorted in descending order. The function takes two parameters: a list of strings (`string_list`) and a positive integer representing the minimum length threshold (`min_length`). The function should return a new list containing only the strings from the input list that have a length greater than or equal to the minimum length threshold. If two strings have the same length, they should be sorted in alphabetical order. The input list will only contain strings and the minimum length threshold will be a positive integer. The function should handle edge cases, such as an empty input list or a minimum length threshold of zero.
"""

from typing import List

def filter_and_sort_strings(string_list: List[str], min_length: int) -> List[str]:
    filtered_strings = []
    
    for string in string_list:
        if len(string) >= min_length:
            filtered_strings.append(string)
    
    filtered_strings.sort(key=lambda x: (-len(x), x))
    
    return filtered_strings