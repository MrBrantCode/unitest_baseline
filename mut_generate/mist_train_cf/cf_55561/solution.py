"""
QUESTION:
Create a function `f(n)` that takes an integer `n` as input and returns a list of length `n`. The element at index `i` should be the factorial of `i` if `i` is even, and the sum of numbers from 1 to `i` if `i` is odd, where `i` starts from 1. The function should have the best time and space complexity possible.
"""

def f(n):
    # Introduce a dictionary to memoize factorials already computed
    fact_memo = {0: 1, 1: 1}  

    # Function to compute factorial
    def factorial(i):
        if i not in fact_memo:
            # store the computed factorial in the memoization dict
            fact_memo[i] = i * factorial(i-1)
        return fact_memo[i]
    
    # Generate the list
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(int(i*(i+1)/2))   # use the formula for summation of n numbers
    return result