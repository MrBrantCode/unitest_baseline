"""
QUESTION:
Write a function called `fibonacci_sequence` that takes a positive integer `n` as input and returns a list containing the first `n` Fibonacci numbers. The function should not accept any other input and should only include the first `n` numbers in the Fibonacci sequence.
"""

def fibonacci_sequence(n):
    fibonacci_list = [0, 1]
    for i in range(n-2):
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)
    return fibonacci_list