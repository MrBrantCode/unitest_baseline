"""
QUESTION:
Create a function `fibonacci_sequence(n)` that generates a Fibonacci sequence of 'n' terms where each term is between 1 and 1000, and no two consecutive terms are consecutive numbers.
"""

def fibonacci_sequence(n):
    lst = []

    # First two numbers of fibonacci sequence
    a, b = 0, 1

    while len(lst) < n:
        # add next number to list
        a, b = b, a + b
        if a >= 1001: 
            a = a % 1000 + 1
            b = a % 1000 + 1
            
        if len(lst) == 0 or len(lst) > 0 and abs(lst[-1] - a) > 1:
            lst.append(a)
    return lst