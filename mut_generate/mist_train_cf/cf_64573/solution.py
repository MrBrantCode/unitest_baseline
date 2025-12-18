"""
QUESTION:
Write a function `next_prime(n)` that returns the smallest prime number greater than `n`, where `n` is an integer. The function should handle cases where `n` is not a non-negative integer and return an error message. The function should use an efficient approach to check for prime numbers.
"""

def next_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2
        return True

    if isinstance(n, int):
        if n < 0:
            return "Error: Input is a negative number."
        elif n == 0 or n == 1 or n == 2:
            return 2
        else:
            n = n + 1 if n % 2 == 0 else n + 2
            while True:
                if is_prime(n):
                    return n
                else:
                    n += 2
    else:
        return "Error: Input is not an integer."