"""
QUESTION:
Write a function `calculate_equation_result(n)` that calculates the result of the equation `(x-1)^2 + (2x-3)^2 + (3x-5)^2 + ... + (nx-(2n-1))^2` modulo 10^9+7, where n is a positive integer and x equals the current index of the equation (1-indexed), using a single for loop and without any built-in mathematical functions or libraries. The function should have a time complexity of O(n) and be able to handle large values of n (up to 10^9) efficiently.
"""

def calculate_equation_result(n):
    result = 0
    modulo = int(1e9) + 7

    for i in range(1, n+1):
        x = i
        result += (x*i - (2*i-1))**2
        result %= modulo

    return result