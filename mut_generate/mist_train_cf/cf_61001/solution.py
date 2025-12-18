"""
QUESTION:
Create a function `harmonic_mean_prime(lst)` that calculates the harmonic mean of the prime numbers in a given list `lst`. The function should ignore non-prime numbers and return 0 if the list contains no prime numbers.
"""

def harmonic_mean(lst):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    prime_lst = [i for i in lst if is_prime(i)]
    if len(prime_lst) == 0:
        return 0
    return len(prime_lst) / sum(1 / i for i in prime_lst)