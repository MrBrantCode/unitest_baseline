"""
QUESTION:
Write a function `fibonacci_sequence(n)` that generates a Fibonacci series up to the n-th term, where n is a user-input value, and calculates the sum of all even numbers in the series. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def fibonacci_sequence(n):
    a, b = 0, 1
    sum_of_evens = 0

    for _ in range(n):
        if a % 2 == 0:
            sum_of_evens += a
        a, b = b, a+b

    return sum_of_evens