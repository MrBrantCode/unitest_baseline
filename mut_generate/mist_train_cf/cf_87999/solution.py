"""
QUESTION:
Write a function named `fibonacci_sum_even` that generates the Fibonacci sequence up to a given number `n` using recursion and returns the sum of all even numbers in the sequence.
"""

def fibonacci_sum_even(n):
    if n <= 0:
        return 0

    fib_sequence = []

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def sum_even(fib_sequence):
        sum = 0
        for num in fib_sequence:
            if num % 2 == 0:
                sum += num
        return sum

    for i in range(1, n + 1):
        fib_sequence.append(fibonacci(i))

    return sum_even(fib_sequence)