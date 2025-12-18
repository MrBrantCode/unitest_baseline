"""
QUESTION:
Create a function `accumulative_even_fibonacci(n)` that takes an integer `n` and returns the Nth term in a sequence formed by the accumulative total of the two antecedent even numbers. The sequence starts with 0 and 2, and each subsequent term is the sum of the previous two terms. The function should return the Nth term of this sequence.
"""

def accumulative_even_fibonacci(n):
    # Initialize the series with two initial even numbers 0 and 2
    series = [0, 2]
    
    # Generate the series up to n terms
    for _ in range(2, n):
        # The next term is the sum of the last two terms in series
        next_term = sum(series[-2:])
        series.append(next_term)
    
    # Return the nth term
    return series[n-1]