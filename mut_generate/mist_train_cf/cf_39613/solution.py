"""
QUESTION:
Write a function `find_square(p: float, n: float) -> float` that returns the square of the input number `p` if the absolute difference between the square and `n` is less than 0.0001 after a certain number of iterations, otherwise return -1. The input parameters `p` and `n` are floating-point numbers where 1 <= p <= 1000 and 0 <= n <= 1000000.
"""

def entrance(p: float, n: float) -> float:
    max_iterations = 1000  
    for _ in range(max_iterations):
        res = p ** 2
        if abs(n - res) < 0.0001:
            return res
        p = (p + n / p) / 2  
    return -1