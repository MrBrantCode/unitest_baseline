"""
QUESTION:
Design a function `median_of_three(a, b, c)` that calculates the median of three given integers. The function should handle exceptions for non-integer inputs and work with both positive and negative integers. If any input is not an integer, the function should return an error message "All inputs must be integers."
"""

def median_of_three(a, b, c):
    try:
        a, b, c = int(a), int(b), int(c)
    except ValueError:
        return "All inputs must be integers."

    numbers = [a, b, c]
    numbers.sort()
    
    return numbers[1]