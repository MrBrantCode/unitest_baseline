"""
QUESTION:
Write a function `compute_rounded_sqrt_iterations` that calculates the average number of iterations needed to find the rounded-square-root of a 14-digit number using the given iterative method. The function should return the average number of iterations rounded to 10 decimal places. 

The function should work with a sample of 1,000,000 randomly selected 14-digit numbers (10^13 ≤ n < 10^14). The initial guess x0 should be determined based on the number of digits in n, with x0 = 2 * 10^((d-1)/2) for odd d and x0 = 7 * 10^((d-2)/2) for even d. The iterative formula is x(k+1) = floor((xk + ceil(n/xk))/2) until x(k+1) = xk.
"""

import numpy as np

def compute_rounded_sqrt_iterations(n):
    d = len(str(n))
    x = 2 * 10 ** ((d - 1) // 2) if d % 2 != 0 else 7 * 10 ** ((d - 2) // 2)
    i = 0
    while True:
        new_x = (x + np.ceil(n / x)) // 2
        i += 1
        if new_x == x:
            return i
        x = new_x