"""
QUESTION:
Create a function called `generate_fibonacci_spiral` that generates a 2D array representing a Fibonacci Spiral. The function should take an integer `n` as input, representing the number of rows (or columns) in the 2D array. The function should return a 2D array where each row represents a Fibonacci sequence up to the nth number, and each number in the sequence is used to define the value in the corresponding position in the array.
"""

def generate_fibonacci_spiral(n):
    def fib_sequence(n):
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib
    
    matrix = []
    for i in range(n):
        row = fib_sequence(n)
        matrix.append(row)
    return matrix