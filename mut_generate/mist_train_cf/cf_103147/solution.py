"""
QUESTION:
Create a Python function `fibonacci_sequence(n)` to print a Fibonacci sequence up to the nth term and return the sum of all the numbers in the sequence. The input `n` is a positive integer and the sequence should start with 0 and 1. The function should return two values: the Fibonacci sequence as a list and the sum of the sequence.
"""

def fibonacci_sequence(n):
    sequence = [0, 1]  
    total_sum = sum(sequence)  
    
    if n <= 2:
        return sequence[:n], total_sum  
    
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]  
        sequence.append(next_term)  
        total_sum += next_term  
    
    return sequence, total_sum 