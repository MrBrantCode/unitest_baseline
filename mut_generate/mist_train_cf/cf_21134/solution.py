"""
QUESTION:
Create a function `check_divisibility(num1, num2)` that determines if `num1` is divisible by `num2` and returns the corresponding results. The function should handle cases where either `num1` or `num2` is negative by printing an error message and returning. If `num1` is divisible by `num2`, the function should print a message stating so, along with the quotient. If `num1` is not divisible by `num2`, the function should print a message stating so, along with the quotient and remainder.
"""

def check_divisibility(num1, num2):
    if num1 < 0 or num2 < 0:
        print("Error: Input numbers cannot be negative.")
        return

    quotient = num1 // num2
    remainder = num1 % num2

    if remainder == 0:
        print(f"{num1} is divisible by {num2}")
        print(f"Quotient: {quotient}")
    else:
        print(f"{num1} is not divisible by {num2}")
        print(f"Quotient: {quotient}, Remainder: {remainder}")