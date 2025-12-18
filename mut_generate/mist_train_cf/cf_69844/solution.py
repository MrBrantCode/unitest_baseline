"""
QUESTION:
Create a function called `swap_characters` that takes a string as input. The function should swap every character at a prime index with the character at the next Fibonacci index in the string. The indexing is zero-based. Implement the prime and Fibonacci number calculations from scratch without using existing libraries.
"""

def swap_characters(s):
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def fibonacci(n):
        if n < 2:
            return n
        else:
            a, b = 0, 1
            for _ in range(n - 1):
                a, b = b, a + b
            return b

    string = list(s)
    length = len(string)
    fib_index = 1
    fib = fibonacci(fib_index)
    for i in range(length):
        if is_prime(i):
            while fib < length and fib <= i:
                fib_index += 1
                fib = fibonacci(fib_index)
            if fib < length:
                string[i], string[fib] = string[fib], string[i]
    return ''.join(string)