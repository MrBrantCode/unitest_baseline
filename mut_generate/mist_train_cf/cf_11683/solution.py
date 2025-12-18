"""
QUESTION:
Write a function `recursive_sum` that computes the sum of a list of integers recursively. The function should not use any built-in functions or operators for summation. It should handle edge cases such as an empty list, a list with only one element, and a list with negative numbers. The function should only use the function call stack to store the necessary information and should not use any additional data structures or variables to store intermediate results.
"""

def recursive_sum(lst):
    # Base case: empty list
    if not lst:
        return 0
    
    # Base case: list with only one element
    if len(lst) == 1:
        return lst[0]
    
    # Recursive case
    return lst[0] + recursive_sum(lst[1:])