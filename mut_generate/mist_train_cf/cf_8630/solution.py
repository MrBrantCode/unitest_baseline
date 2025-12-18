"""
QUESTION:
Design a function `fib_recursive(n)` that generates the Fibonacci sequence up to a given index `n` and computes the sum of all the Fibonacci numbers up to `n`. The function should handle negative indices by returning an empty sequence and a sum of 0. Implement the function using memoization to achieve a time complexity of O(n). The function should be able to handle large values of `n` efficiently. The function should return a tuple containing the Fibonacci sequence as a single number (not a list) and the sum of the Fibonacci sequence.
"""

fib_dict = {0: (0, 0), 1: (1, 1)}

def fib_recursive(n):
    if n < 0:
        return 0, 0
    
    if n in fib_dict:
        return fib_dict[n]
    
    fib_n_1, sum_n_1 = fib_recursive(n-1)
    fib_n_2, sum_n_2 = fib_recursive(n-2)
    
    fib_n = fib_n_1 + fib_n_2
    sum_n = sum_n_1 + sum_n_2 + fib_n
    
    fib_dict[n] = (fib_n, sum_n)
    
    return fib_n, sum_n