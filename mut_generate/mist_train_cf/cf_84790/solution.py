"""
QUESTION:
Write a function `LucasNumber(n)` that generates the nth Lucas number, where the Lucas numbers are defined by the recurrence relation `Lucas(n) = Lucas(n-1) + Lucas(n-2)` for `n >= 2` with initial conditions `Lucas(0) = 2` and `Lucas(1) = 1`. The function should take a non-negative integer `n` as input and return the corresponding Lucas number. If `n` is negative, the function should return an error message "Input must be a positive integer".
"""

def lucas_number(n):
    if n < 0:
        return "Input must be a positive integer"
    elif n == 0:
        return 2
    elif n == 1:
        return 1
        
    lucas_numbers = [0] * (n + 1)
    lucas_numbers[0] = 2
    lucas_numbers[1] = 1

    for i in range(2, n + 1):
        lucas_numbers[i] = lucas_numbers[i-1] + lucas_numbers[i-2]
        
    return lucas_numbers[n]