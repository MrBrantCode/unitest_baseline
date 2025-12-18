"""
QUESTION:
Write a function `cube_primes(num)` that generates a list of numbers that are the cube of all prime numbers between 1 and the number `num`.
"""

def cube_primes(num):
    def is_prime(n):
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False    
        return True

    return [i**3 for i in range(2, num + 1) if is_prime(i)]