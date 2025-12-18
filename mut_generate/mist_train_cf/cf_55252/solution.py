"""
QUESTION:
Write a function `find_sum(x)` that calculates the sum of all integers from 1 to `x` (inclusive) that are divisible by 3 or 5. The function should accommodate negative integers by treating them as their absolute values. It should also include error handling to return an error message when the input is not an integer.
"""

def find_sum(x):
    try:
        x = abs(int(x))  # Make negative integers positive and ensure x is an integer
        sum = 0
        for i in range(1, x+1):  # x+1 is used so that x is included in the calculation
            if i % 3 == 0 or i % 5 == 0:
                sum += i
        return sum
    except ValueError:  # Catch non-integer inputs
        return "Error: Input should be an integer"