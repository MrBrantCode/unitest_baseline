"""
QUESTION:
Create a recursive function named `print_even_numbers(n)` that prints even numbers from `n` down to 0 in descending order. The function should only print even numbers and should not print any number more than once. The input to the function will be a non-negative integer `n`. The function should not use any loops.
"""

def entrance(n):
    if n < 0:
        return
    if n % 2 == 0:
        print(n)
    entrance(n - 2)