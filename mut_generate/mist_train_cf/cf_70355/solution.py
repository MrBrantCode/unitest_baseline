"""
QUESTION:
Create a function `fibo_sum(n)` that calculates the sum of Fibonacci numbers up to the nth number, only including numbers that are divisible by 3. The Fibonacci sequence starts with two 1's, and the first term is counted as the first 1.
"""

def fibo_sum(n):
    def fibo(n):
        x, y = 1, 1
        for _ in range(n):
            yield x
            x, y = y, x + y

    return sum(x for x in fibo(n) if x % 3 == 0)