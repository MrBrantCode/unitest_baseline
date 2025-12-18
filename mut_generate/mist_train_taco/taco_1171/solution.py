"""
QUESTION:
Write a program which reads two integers a and b, and calculates the following values:

* a ÷ b: d (in integer)
* remainder of a ÷ b: r (in integer)
* a ÷ b: f (in real number)

Constraints

* 1 ≤ a, b ≤ 109

Input

Two integers a and b are given in a line.

Output

Print d, r and f separated by a space in a line. For f, the output should not contain an absolute error greater than 10-5.

Example

Input

3 2


Output

1 1 1.50000
"""

def calculate_division_values(a: int, b: int) -> tuple:
    d = a // b
    r = a % b
    f = a / b
    return d, r, round(f, 5)