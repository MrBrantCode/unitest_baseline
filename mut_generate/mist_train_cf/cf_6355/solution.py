"""
QUESTION:
Generate a function named `generate_fibonacci` that generates the Fibonacci sequence up to the nth term without using recursion and any additional data structures beyond what's necessary to store the sequence. Note: It's not possible to achieve a time complexity of O(1) for this problem, so aim for the best achievable time complexity.
"""

def generate_fibonacci(n):
    if n <= 0:
        return []
    
    if n == 1:
        return [0]
    
    if n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    
    for i in range(2, n):
        next_term = sequence[i-1] + sequence[i-2]
        sequence.append(next_term)
    
    return sequence