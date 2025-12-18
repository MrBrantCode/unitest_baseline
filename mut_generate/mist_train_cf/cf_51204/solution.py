"""
QUESTION:
Write a function named `fibonacci_squared` that takes an integer `n` as input, calculates the squares of the first `n` Fibonacci numbers, and returns them as a list. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. If `n` is less than or equal to 0, the function should return an empty list.
"""

def fibonacci_squared(n):
    if n <= 0: 
        return []
    
    fibonacci_sequence = [0, 1] 
    squared_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
        next_element = fibonacci_sequence[-1] + fibonacci_sequence[-2] 
        fibonacci_sequence.append(next_element) 
        squared_sequence.append(next_element ** 2) 

    return squared_sequence[:n]