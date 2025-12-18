"""
QUESTION:
Write a function `generate_fibonacci_sequence(n)` that generates a Fibonacci sequence up to the nth number and returns it as a list, with a time complexity of O(n) and a space complexity of O(1).
"""

def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]  

    if n < 2:
        return fibonacci_sequence[:n + 1]

    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence