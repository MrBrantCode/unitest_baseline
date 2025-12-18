"""
QUESTION:
Analyze the time and space complexity of the given Fibonacci function with caching. 

The function is defined as `fibonacci(n, computed = {0: 0, 1: 1})`, where `computed` is a dictionary used to store previously calculated Fibonacci numbers. 

Assume that this function can be parallelized such that `fibonacci(n-1)` and `fibonacci(n-2)` can run simultaneously. How does this affect the time complexity? 

Implement a performance analysis that compares the execution times of the original and parallel versions for inputs of 2^n, where n ranges from 0 to 20.
"""

def fibonacci(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fibonacci(n-1, computed) + fibonacci(n-2, computed)
    return computed[n]