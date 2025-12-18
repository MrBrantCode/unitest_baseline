"""
QUESTION:
Implement a recursive function named `print_sequence` that prints a sequence of numbers from 0 to a given number `n` (inclusive) in ascending order. The function should take one integer argument `n` and include a base case to prevent infinite recursion. If `n` is negative, the function should print an error message instead of the sequence.
"""

def print_sequence(n):
    # Base cases
    if n < 0:
        print("Error: Negative input.")
        return
    elif n == 0:
        print(0)
        return

    # Recursive case
    else:
        print_sequence(n - 1)  # recursive call
        print(n)