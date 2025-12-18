"""
QUESTION:
Write a function named `fibonacci` to generate a list of Fibonacci sequence up to the nth term using recursion. The function should take an integer n as input and return a list of integers. The Fibonacci sequence should be defined as: 
- If n is 0 or less, return an empty list.
- If n is 1, return a list containing only 0.
- If n is 2, return a list containing 0 and 1.
- For n greater than 2, calculate each term as the sum of the last two preceding terms.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibSeq = fibonacci(n - 1)
        fibSeq.append(fibSeq[-1] + fibSeq[-2])
        return fibSeq