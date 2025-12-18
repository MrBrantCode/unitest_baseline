"""
QUESTION:
Write a function `generate_fibonacci_sequence(n)` that generates a Fibonacci sequence up to the nth number in the sequence, where the next number is the sum of the two preceding ones. The function should have a time complexity of O(n) and a space complexity of O(1), and it should return the Fibonacci sequence as a list.
"""

def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]  

    if n < 2:
        return fibonacci_sequence[:n + 1]

    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence