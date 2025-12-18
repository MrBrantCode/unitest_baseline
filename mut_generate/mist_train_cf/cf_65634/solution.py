"""
QUESTION:
Write a function named `fibonacci` that generates the Fibonacci sequence up to the nth term. The function should be efficient in terms of time and space complexity and should utilize data structures effectively. Implement user input validation to ensure that the input is a positive integer.
"""

def fibonacci(n):
    sequence = [0, 1]
    while(len(sequence) < n):
        sequence.append(sequence[-1]+sequence[-2])
    return sequence