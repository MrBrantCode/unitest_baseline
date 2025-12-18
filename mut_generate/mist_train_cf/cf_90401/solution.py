"""
QUESTION:
Write a function called `print_right_triangle(n)` that prints a right-angled triangle with stars, where the number of rows and columns is equal to the input number `n`. The input number `n` should be between 5 and 15 (inclusive). The function should have a time complexity of O(n^2).
"""

def print_right_triangle(n):
    if n < 5 or n > 15:
        print("Input number should be between 5 and 15 (inclusive)")
        return

    for i in range(1, n+1):
        print("*" * i)