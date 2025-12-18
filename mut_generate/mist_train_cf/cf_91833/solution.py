"""
QUESTION:
Create a function named `fibonacci_sequence(n)` that takes a positive integer `n` as input. The function should generate and return a Fibonacci sequence up to the nth term and also return the sum of all numbers in the sequence.
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