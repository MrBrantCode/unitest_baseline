"""
QUESTION:
Write a function `fibonacci_sequence(n)` that generates the Fibonacci sequence up to the nth number, given that n is a positive integer less than or equal to 10^6. The function should have a time complexity of O(n) and a space complexity of O(n), where the output is a list containing the Fibonacci sequence up to the nth number, defined as a sequence where the first and second numbers are both 1, and each subsequent number is the sum of the two preceding numbers.
"""

def fibonacci_sequence(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib_sequence = [1, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return fib_sequence