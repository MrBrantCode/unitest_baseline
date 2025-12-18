"""
QUESTION:
Create a function `get_prime_fibos` that generates prime Fibonacci numbers and their respective positions in the Fibonacci series up to a given number `upto`. The function should optimize its execution for efficiency.
"""

def get_prime_fibos(upto):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def fibonacci():
        a, b = 0, 1
        yield a
        yield b
        while True:
            a, b = b, a + b
            yield b

    pos = 0
    for fibo in fibonacci():
        if fibo > upto:
            break
        if is_prime(fibo):
            yield pos, fibo
        pos += 1