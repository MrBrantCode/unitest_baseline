"""
QUESTION:
Write a function `fibonacci_sum_of_squares(n)` that calculates the accumulated total of the square values from the Fibonacci series encompassing up to n elements. The function should return the sum of squares of Fibonacci numbers F(0)^2 + F(1)^2 + F(2)^2 + ... + F(n)^2. 

Note: The function is only required to work for non-negative integers n.
"""

def fibonacci_sum_of_squares(n):
    if n <= 1:
        return n
    else:
        sum = 0
        a, b = 0, 1
        for _ in range(n+1):
            sum += a * a
            a, b = b, a + b
        return sum