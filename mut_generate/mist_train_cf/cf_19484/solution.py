"""
QUESTION:
Implement a function `fibonacci(n)` that calculates the Fibonacci sequence up to the nth number using an iterative approach without recursion. The function should return a list of integers representing the Fibonacci sequence, and it should handle invalid inputs (n <= 0) by returning an error message.
"""

def fibonacci(n):
    if n <= 0:
        return "Invalid input! Please provide a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers
    
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])  # Generate the next Fibonacci number by summing the previous two
        
    return sequence