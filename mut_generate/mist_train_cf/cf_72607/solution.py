"""
QUESTION:
Create a function perfect_cubes_primes(n) that returns a list of perfect cubes of prime numbers less than the given number n. The function should only consider prime numbers up to the cube root of n.
"""

def perfect_cubes_primes(n):
    def is_prime(x):
        if x <= 1:
            return False
        if x <= 3:
            return True
        if x % 2 == 0 or x % 3 == 0:
            return False
        i = 5
        while i * i <= x:
            if x % i == 0 or x % (i + 2) == 0:
                return False
            i += 6
        return True

    cubes = []
    for i in range(2, int(n ** (1/3)) + 1):
        if is_prime(i):
            cube = i ** 3
            if cube < n:
                cubes.append(cube)
    return cubes