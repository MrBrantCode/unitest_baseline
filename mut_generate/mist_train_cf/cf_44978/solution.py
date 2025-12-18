"""
QUESTION:
Create two functions, `cumulative_total(n)` and `cumulative_product(n)`, that calculate the cumulative total and product of all positive integers from 1 to a specified number `n`. The functions should handle edge cases where `n` may be zero or a non-integer. If `n` is negative or not an integer, return an error message; otherwise, return the cumulative total and product.
"""

def cumulative_total(n):
    if isinstance(n, int) and n >= 0:  
        total = 0
        for i in range(1, n+1):
            total += i
        return total
    else:
        return "Input must be a non-negative integer"

def cumulative_product(n):
    if isinstance(n, int) and n >= 0:  
        product = 1
        for i in range(1, n+1):
            product *= i
        return product
    else:
        return "Input must be a non-negative integer"