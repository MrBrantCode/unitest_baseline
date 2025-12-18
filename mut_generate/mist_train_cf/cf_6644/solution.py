"""
QUESTION:
Create a recursive function called `fibonacci` that generates the n-th Fibonacci number and calculates the sum of all Fibonacci numbers from 1 to n. The function should have a time complexity of O(2^n) and should be implemented using only a single recursive function. However, note that having a single recursive function also calculates the sum from 1 to n is a contradictory requirement as it can't directly return two values (nth fibonacci and the sum of all numbers).
"""

def fibonacci(n, total_sum=0, i=1, fib_prev=0, fib_curr=1):
    if i > n:
        return fib_prev, total_sum
    else:
        total_sum += fib_curr
        return fibonacci(n, total_sum, i+1, fib_curr, fib_prev + fib_curr)