"""
QUESTION:
Write a function named `fibonacci_sum_even(n)` that takes an integer `n` as input and returns the sum of all even-valued terms in the Fibonacci sequence up to the nth term. The input `n` should be between 1 and 1000, inclusive.
"""

def fibonacci_sum_even(n):
    if n < 1 or n > 1000:
        return "Invalid input. Please provide a value for n between 1 and 1000."

    fib_sequence = [1, 1]  
    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]  
        fib_sequence.append(next_term)  

    even_sum = sum([term for term in fib_sequence if term % 2 == 0])  

    return even_sum