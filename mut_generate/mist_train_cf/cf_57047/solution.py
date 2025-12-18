"""
QUESTION:
Create a function `find_nth_in_series(n)` that finds the nth term of a series where each term is the sum of the last two even terms, with the first two terms being 2 and 4. The function should handle cases where n is less than 1 and return an error message for non-positive integers.
"""

def find_nth_in_series(n):
    if n<1:
      return "Input should be a positive integer"
    n -= 1  # since we are using 0-based indexing
    a, b = 2, 4 # Initializing first two numbers of the series.
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(2, n+1): 
        a, b = b, a+b 
    return b