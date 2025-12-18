"""
QUESTION:
Create a function called `compound_interest` that calculates the compound interest rate given the initial principal amount P, the annual interest rate r, the number of times compounding occurs in a year n, and the number of years t. The function should return an error message if any of the input values are negative or if P is zero. Otherwise, the function should return the compound interest amount rounded to the nearest whole number.
"""

def compound_interest(P, r, n, t):
    if P < 0 or r < 0 or n < 0 or t < 0:
        return "Error: Values cannot be negative."
    if P == 0:
        return "Error: Initial principal amount cannot be zero."

    A = P * (1 + r/n) ** (n*t)
    A = round(A)
    return A