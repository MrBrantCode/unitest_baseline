"""
QUESTION:
Create a function `compare_numbers(a, b)` that takes two numbers as input and returns a string indicating whether `a` is 'lower', 'higher', or 'equal' to `b`. The function should be able to handle decimal values and numbers in scientific notation, and should have a time complexity of O(1).
"""

def entance(a, b):
    a = float(a)
    b = float(b)
    
    if a < b:
        return 'lower'
    elif a > b:
        return 'higher'
    else:
        return 'equal'