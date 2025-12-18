"""
QUESTION:
Write a function `lucasNumber(n)` to calculate the nth term in the Lucas series. The Lucas series is defined with the first two terms as 2 and 1, and each subsequent term is the sum of the previous two terms. The function should take an integer `n` as input and return the nth term. The solution should have a time complexity of O(n) and space complexity of O(1), without using recursion or built-in mathematical functions or libraries.
"""

def lucas_number(n):
    # Base cases for n = 0 and n = 1
    if n == 0:
        return 2
    if n == 1:
        return 1

    # Initialize variables for the previous two terms
    prev_prev = 2
    prev = 1

    # Calculate the nth term using a loop
    for _ in range(2, n + 1):
        current = prev + prev_prev
        prev_prev = prev
        prev = current

    return prev