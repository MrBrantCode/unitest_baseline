"""
QUESTION:
Write a function named `reverse_fibonacci` that takes a list of integers representing a Fibonacci sequence as input and returns a new list containing the reversed Fibonacci sequence without using any built-in reversing functions. The function should have linear time complexity.
"""

def reverse_fibonacci(fib_sequence):
    length = len(fib_sequence)
    reversed_sequence = [0]*length

    for i in range(length):
        reversed_sequence[i] = fib_sequence[length-i-1]
        
    return reversed_sequence