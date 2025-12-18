"""
QUESTION:
Write a function called `generate_fibonacci(n)` that generates an array of Fibonacci numbers with n numbers. The function should not use recursion, should have a time complexity of O(n), and should use a constant amount of extra space, regardless of the value of n. The Fibonacci sequence is defined as the sum of the two previous numbers in the sequence, starting with 0 and 1.
"""

def generate_fibonacci(n):
    if n <= 0:
        return []

    fibonacci = [0] * n
    fibonacci[0] = 0
    if n > 1:
        fibonacci[1] = 1

    for i in range(2, n):
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

    return fibonacci