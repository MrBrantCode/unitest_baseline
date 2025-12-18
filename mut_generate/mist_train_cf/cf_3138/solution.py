"""
QUESTION:
Write a function `find_prime_chars` that takes two strings as input and returns a list of characters that are present in the first string and have ASCII values greater than 100 that are prime numbers. Use the Sieve of Eratosthenes algorithm to generate prime numbers up to a sufficient limit.
"""

def find_prime_chars(s1, s2):
    def sieve_of_eratosthenes(n):
        is_prime = [True] * (n+1)
        is_prime[0] = is_prime[1] = False

        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n+1, p):
                    is_prime[i] = False
            p += 1

        return is_prime

    primes = sieve_of_eratosthenes(1000)

    prime_chars = []
    for char in s1:
        ascii_val = ord(char)
        if ascii_val > 100 and primes[ascii_val]:
            prime_chars.append(char)

    return prime_chars