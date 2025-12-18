"""
QUESTION:
Create a function `generate_matrix(n)` that generates a matrix where every row represents the prime factors of the respective integer from 2 to `n` in ascending order. The function should return a 2D list where each sublist contains the prime factors of the corresponding integer.
"""

def generate_matrix(n):
    def prime_factors(num):
        i = 2
        factors = []
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                factors.append(i)
        if num > 1:
            factors.append(num)
        return factors

    matrix = []
    for i in range(2, n+1):
        matrix.append(prime_factors(i))
    return matrix