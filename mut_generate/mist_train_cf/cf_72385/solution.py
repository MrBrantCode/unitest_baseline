"""
QUESTION:
Create a function named `fibonacci` that takes an integer `n` as input and returns a list containing the Fibonacci series up to the `n`th term. The function should handle potential input errors, including non-integer and non-positive inputs, and be scalable for large values of `n`. The output list should include the Fibonacci series from the first term up to the `n`th term.
"""

def fibonacci(n):
    if type(n) != int or n <= 0:
        print("Input should be a positive integer")
        return None

    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonacci_series = [0, 1]
    
    for i in range(2, n):
        next_element = fibonacci_series[i-1] + fibonacci_series[i-2]
        fibonacci_series.append(next_element)
        
    return fibonacci_series