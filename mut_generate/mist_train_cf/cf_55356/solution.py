"""
QUESTION:
Construct a function `sort_values(lst)` that filters out all even numbers from a given list, then sorts the remaining odd numbers in ascending order. If the input list is empty or only contains even numbers, the function should return `None`.
"""

def sort_values(lst):
    if not lst:  
        return None
    sorted_odd_numbers = sorted([i for i in lst if i%2 != 0])  
    if not sorted_odd_numbers:  
        return None
    return sorted_odd_numbers