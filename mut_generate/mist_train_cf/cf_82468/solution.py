"""
QUESTION:
Create a function called `recursive_sum` that takes a list of numbers as input and returns the sum of all numbers in the list using a recursive approach. The function should handle the base case where the input list is empty and return 0 in such cases.
"""

def recursive_sum(lst):
    # Base case: if the list is empty, just returns 0
    if not lst:
        return 0
    # Recursive case: adds the first number in the list to the result of recursively
    # calling this function on the rest of the list
    else:
        return lst[0] + recursive_sum(lst[1:])