"""
QUESTION:
Create a function `prime_factors_matrix(n)` that generates a matrix where each row represents the prime factors of the corresponding number starting from 2 up to `n`. The function should return a list of lists, where each sublist contains the prime factors of a number. Note that the length of the sublists may not be uniform. The input `n` must be greater than or equal to 2.
"""

def prime_factors_matrix(n):
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