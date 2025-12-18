"""
QUESTION:
Create a function `print_right_triangle(n)` that prints a right-angled triangle of stars with `n` rows and columns. The function should take an integer `n` as input, where `5 ≤ n ≤ 15`. The function should not take any additional inputs and should print the triangle directly.
"""

def entance(n):
    if n < 5 or n > 15:
        print("Input number should be between 5 and 15 (inclusive)")
        return

    for i in range(1, n+1):
        print("*" * i)