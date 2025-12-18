"""
QUESTION:
Write a function `solve(n, m)` that takes two integers `n` and `m` as input and returns their greatest common divisor (GCD) if both `n` and `m` are Mersenne prime numbers. A Mersenne prime is a prime number that can be written in the form `2^P-1`, where `P` is also a prime number. The function should not use any built-in functions for GCD computation. The input integers `n` and `m` should be validated to check if they are both Mersenne prime numbers before calculating their GCD.
"""

def solve(n, m):
    def is_prime(num):
        if num <= 1 or (num % 2 == 0 and num > 2): 
            return False
        return all(num % i for i in range(3, int(num**0.5) + 1, 2))

    def is_mersenne_number(num):
        i = 1
        while True:
            mersenne_num = 2 ** i - 1
            if mersenne_num > num:
                return False
            if mersenne_num == num:
                return True
            i += 1
        return False

    def is_mersenne_prime(num):
        return is_mersenne_number(num) and is_prime(num)

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    if is_mersenne_prime(n) and is_mersenne_prime(m):
        return gcd(n, m)