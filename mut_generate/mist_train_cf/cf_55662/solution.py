"""
QUESTION:
Create a function `fibo_modified(n)` that generates a modified Fibonacci series up to the nth term. The series starts with 0 and 1, and each subsequent term is the product of the previous two terms if they are both even and non-zero; otherwise, it is the sum of the previous two terms.
"""

def fibo_modified(n):
    """
    Generates a modified Fibonacci series up to the nth term.
    The series starts with 0 and 1, and each subsequent term is the product of the previous two terms 
    if they are both even and non-zero; otherwise, it is the sum of the previous two terms.
    
    Parameters:
    n (int): The number of terms in the series.
    
    Returns:
    list: A list of integers representing the modified Fibonacci series.
    """
    fib = [0, 1]
    while len(fib) < n+1:
        if (fib[-1] % 2 == 0) and (fib[-2] % 2 == 0) and fib[-1]!=0 and fib[-2]!=0:
            fib.append(fib[-1] * fib[-2])
        else:
            fib.append(fib[-1] + fib[-2])
    return fib