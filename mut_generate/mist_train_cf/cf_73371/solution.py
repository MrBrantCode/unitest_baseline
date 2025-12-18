"""
QUESTION:
Create a function `custom_prime_factorial` that takes five positive integers `a`, `b`, `c`, `d`, and `e` as input. The function should generate a list of prime numbers from the range `[a, b]` that are not divisible by `c`, compute the factorial of each prime number multiplied by `e`, and return the `d`th smallest result. If the `d`th value does not exist or the inputs are invalid, return `-1`. The function must handle cases where the input values may cause the function to crash, such as large numbers for the factorial calculation.
"""

def custom_prime_factorial(a, b, c, d, e):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqr = int(n**0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    if a > b or a < 1 or b < 1 or c < 1 or d < 1 or e < 1:
        return -1

    ListA = [x for x in range(a, b+1) if is_prime(x) and x % c != 0]
    ListB = [factorial(x) * e for x in ListA]

    ListB.sort()
    
    if len(ListB) < d or d <= 0:
        return -1

    return ListB[d-1]