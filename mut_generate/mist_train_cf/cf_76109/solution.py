"""
QUESTION:
Write a function `rearrange_numbers(lst)` that rearranges the elements in the given list `lst` such that every prime number is followed by the next non-prime number. The function should return the rearranged list. Assume that a prime number is a number that has only two distinct natural number divisors: 1 and itself.
"""

def rearrange_numbers(lst):
    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while (i * i) <= n:
            if (n % i == 0 or n % (i + 2) == 0):
                return False
            i += 6
        return True

    """Rearrange list so every prime number is followed by the next non-prime number."""
    primes = [num for num in lst if is_prime(num)]
    non_primes = [num for num in lst if not is_prime(num)]
    result = []
    for i in range(len(primes)):
        result.append(primes[i])
        if i < len(non_primes):
            result.append(non_primes[i])
    return result + non_primes[len(primes):]