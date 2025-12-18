"""
QUESTION:
Create a function named `positive_odd_cubes_sum` that takes a list of numbers as input. The function should return the sum of the cubes of numbers in the list that are both odd and positive, ignoring any non-integer or negative numbers. If the input list is empty, the function should return 0.
"""

def positive_odd_cubes_sum(lst):
    if not lst:
        return 0
    
    result = 0
    for num in lst:
        if isinstance(num, int) and num > 0 and num % 2 == 1:
            result += num ** 3
            
    return result