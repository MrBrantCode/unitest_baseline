"""
QUESTION:
Write a function `generate_fibonacci(n)` that generates a list of Fibonacci numbers up to the nth number in the sequence. The function should return a list of integers, starting with 0 and 1, where each subsequent number is the sum of the previous two.
"""

def generate_fibonacci(n):
    fibonacci_list = [0, 1]
    for i in range(2, n+1):
        fibonacci_list.append(fibonacci_list[i-2] + fibonacci_list[i-1])
    return fibonacci_list