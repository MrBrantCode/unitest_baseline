"""
QUESTION:
Write a function named `fibonacci_numbers` that takes an integer `N` as input and returns a list of Fibonacci numbers up to the Nth number. The function should not use recursion and should have a space complexity of O(1), not using extra space that scales with input size, or O(N) if it is not possible.
"""

def fibonacci_numbers(N):
    if N <= 0:
        return

    fib_numbers = [0, 1]  # initialize the first two Fibonacci numbers
    for i in range(2, N):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])  # calculate the next Fibonacci number
    return fib_numbers