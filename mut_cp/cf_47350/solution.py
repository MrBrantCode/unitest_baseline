"""
ORIGINAL QUESTION:
Write a function called `solve_problem(lst)` that takes a list of integers as input, removes duplicates, sorts the remaining elements in descending order, and returns the result. Additionally, write two more functions: `calculate_delta(lst)` and `calculate_sum(lst)`, which calculate the difference between the two largest elements and the sum of the two smallest elements in the list respectively. The list must contain at least two elements for these functions to work correctly.
"""

def entrance(lst):
    lst = list(set(lst)) 
    lst.sort(reverse=True) 
    return lst

def calculate_delta(lst):
    if len(lst) < 2:
        return "The list must contain at least two elements"
    else:
        return lst[0] - lst[1]

def calculate_sum(lst):
    if len(lst) < 2:
        return "The list must contain at least two elements"
    else:
        return lst[-1] + lst[-2]