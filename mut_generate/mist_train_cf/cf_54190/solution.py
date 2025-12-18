"""
QUESTION:
Write a function `fibonacci(n)` that generates a Fibonacci sequence up to a given number `n`. The sequence should include the first two numbers (0 and 1) and subsequent numbers should be the sum of the previous two. The sequence should stop once a number greater than `n` is reached, and that number should not be included in the output.
"""

def fibonacci(n):
    """
    Generates a Fibonacci sequence up to a given number n.
    
    Args:
    n (int): The maximum number up to which the Fibonacci sequence is generated.
    
    Returns:
    list: A list of Fibonacci numbers up to n.
    """
    fib_seq = [0, 1]
    while fib_seq[-1] <= n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    if fib_seq[-1] > n:   
        fib_seq.pop()
    return fib_seq