"""
QUESTION:
Write a function named `solve` that takes a list of integers as input, calculates the average, and returns a tuple containing the average as a floating-point number and the number closest to the average. If two numbers are equally distant from the average, return the smaller number. If the list is empty, return (0, None). The list can have up to 10,000 numbers ranging from -10,000 to 10,000.
"""

def solve(lst):
    if not lst:
        return 0, None

    avg = sum(lst) / len(lst)
    closest = min(lst, key=lambda x: (abs(x - avg), x))
    
    return avg, closest