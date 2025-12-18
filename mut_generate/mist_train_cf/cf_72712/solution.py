"""
QUESTION:
Create a function named `calculate_mode` that takes a list of floats as input. The function should return the mode of the list, which is the value that appears most frequently. If multiple modes exist, return a list of these modes in ascending order. If the input list is empty, return -1. All float values should be rounded to 2 decimal places. The function should also handle edge cases where the list contains only one unique value or all elements appear the exact same number of times.
"""

from collections import Counter

def calculate_mode(lst):
    if not lst: 
        return -1  
    elif len(set(lst)) == 1: 
        return round(lst[0], 2)  
    else: 
        count_dict = Counter(round(num, 2) for num in lst)
        max_count = max(count_dict.values())
        modes = [k for k, v in count_dict.items() if v == max_count]
        return sorted(modes)