"""
QUESTION:
Write a function called `print_altered_primes` that prints every `x`th prime number within a range of integers from 1 to 100, where `x` is the input alternation pattern. The function should optimize for performance by avoiding unnecessary calculations or iterations. The alternation pattern `x` will be provided as an input to the function.
"""


def print_altered_primes(alteration):
    def is_prime(n):
        """Check if number is prime or not."""
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

    primes = [i for i in range(1, 101) if is_prime(i)]
    for i in range(alteration-1, len(primes), alteration):
        print(primes[i])