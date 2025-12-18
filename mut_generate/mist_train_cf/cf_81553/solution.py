"""
QUESTION:
Write a function `sum_of_prime(matrix)` that takes a multidimensional array of integers as input and returns the sum of all prime numbers in the matrix. The function should handle matrices of varying sizes and structures.
"""

def sum_of_primes(matrix):
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    total = 0
    for row in matrix:
        for num in row:
            if is_prime(num):
                total += num
                
    return total