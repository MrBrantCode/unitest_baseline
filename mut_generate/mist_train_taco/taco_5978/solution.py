"""
QUESTION:
Impliment the reverse function, which takes in input n and reverses it. For instance, `reverse(123)` should return `321`. You should do this without converting the inputted number into a string.
"""

def reverse_integer(n: int) -> int:
    m = 0
    while n > 0:
        n, m = n // 10, m * 10 + n % 10
    return m