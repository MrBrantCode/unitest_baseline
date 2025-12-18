"""
QUESTION:
Implement the function `recursive_function(num)` that calculates the sum of numbers from 0 to `num` using recursive calls, while considering the limitations and potential errors related to excessive recursion in Python. The function should demonstrate the effects of recursive calls on stack memory utilization and potential stack overflow errors when the maximum recursion depth is exceeded. Ensure the function raises a `RecursionError` when the number of recursive calls exceeds the maximum limit.
"""

def recursive_function(num):
    if num == 0:  # Base case
        return 0
    else:
        return num + recursive_function(num - 1)  # Recursive call