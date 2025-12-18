"""
QUESTION:
Write a function `fibonacci_golden_ratio(n)` that generates the Fibonacci series up to the nth term and calculates the nth term's golden ratio. The golden ratio is calculated as the ratio of the nth term to the (n-1)th term, assuming n > 1. Use dynamic programming to optimize performance and ensure the algorithm can handle large inputs efficiently. Provide a solution that can return both the entire Fibonacci series and the golden ratio.
"""

def fibonacci_golden_ratio(n):
    # Handling cases for n=0, n=1 and n=2
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    # Initialize fibonacci series using dynamic programming
    fib_seq = [0]*n
    fib_seq[0] = 0
    fib_seq[1] = 1

    # Generate fibonacci series upto nth term
    for i in range(2, n):
        fib_seq[i] = fib_seq[i-1] + fib_seq[i-2]

    # Golden Ratio of nth term
    golden_ratio = fib_seq[n-1] / fib_seq[n-2]

    return fib_seq, golden_ratio