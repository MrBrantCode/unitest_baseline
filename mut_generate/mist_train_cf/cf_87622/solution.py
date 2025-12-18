"""
QUESTION:
Create a function `generate_pythagorean_triples` to generate Pythagorean Triples up to a given limit. The generated triples must satisfy the following conditions: 
- The sum of the three sides is equal to or less than 50.
- The product of the three sides is a prime number.
- The sides form an arithmetic progression with a common difference of 2.
- The hypotenuse is a multiple of 5.
- The product of the two shorter sides is divisible by 3.
- The sum of the three sides is a perfect square.
"""

import math

def generate_pythagorean_triples(limit):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_divisible_by_3(n):
        return n % 3 == 0

    def is_perfect_square(n):
        sqrt_n = int(math.sqrt(n))
        return sqrt_n * sqrt_n == n

    triples = []
    for a in range(1, limit+1):
        for b in range(a+2, limit+1, 2):
            c = math.sqrt(a**2 + b**2)
            if c == int(c) and c <= limit and a + b + c <= 50 and is_prime(a * b * c) and is_divisible_by_3(a * b) and (a + b + c) ** 0.5 % 1 == 0 and c % 5 == 0:
                triples.append((a, b, int(c)))
    return triples