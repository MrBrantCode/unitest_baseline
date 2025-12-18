"""
QUESTION:
Write a Python function named `process_input(n)` that takes a single argument `n` and performs the following operations:

- Validate if `n` is a non-negative integer.
- If `n` is valid, determine and return whether `n` is odd or even and whether `n` is a prime number or composite number.
- If `n` is not valid, print an error message.

Restrictions: The function should handle the cases where `n` is 0 or 1.
"""

def process_input(n):
    def check_odd_even(n):
        if n % 2 == 0:
            return "Even"
        else:
            return "Odd"

    def check_prime(n):
        if n == 0 or n == 1:
            return "Neither Prime nor Composite"
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return "Composite"
        return "Prime"

    if not isinstance(n, int) or n < 0:
        print("Invalid Input! Please enter a non-negative integer.")
        return
    return f"Odd/Even: {check_odd_even(n)}\nPrime/Composite: {check_prime(n)}"