"""
QUESTION:
Write a function `fibonacci_squares(n)` to generate two lists: one containing the first 'n' numbers in the Fibonacci sequence and another containing the squares of these numbers. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. The function should return both lists.
"""

def fibonacci_squares(n):
    # Generating Fibonacci sequence
    fibonacci_list = [0, 1]
    [fibonacci_list.append(fibonacci_list[-2] + fibonacci_list[-1]) for _ in range(n - 2)]
    # Squaring the Fibonacci sequence
    squared_list = [i**2 for i in fibonacci_list]
    
    return fibonacci_list, squared_list