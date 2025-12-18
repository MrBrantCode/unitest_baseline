"""
QUESTION:
Implement a function `fibonacci(n)` that computes the Fibonacci series until the nth term. The function should take an integer `n` as input and return a list of the first `n` elements in the Fibonacci series, following the mathematical rule that each element is the sum of the two preceding ones. The function should handle cases where `n` is less than or equal to 2 by returning the first `n` elements.
"""

def fibonacci(n):
    #The first two terms
    fibonacci_series = [0, 1]

    #Check if n is less than or equal to 2
    if n<=2:
        return fibonacci_series[:n]
      
    else:
        # Generating the subsequent terms
        for i in range(2, n):
            next_element = fibonacci_series[i-1] + fibonacci_series[i-2]
            fibonacci_series.append(next_element)

        return fibonacci_series