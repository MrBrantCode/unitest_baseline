"""
QUESTION:
Write a function `print_twin_primes(start, end)` that takes two integers `start` and `end` as input, where `start` is less than or equal to `end`, and prints all twin primes between `start` and `end` (inclusive). A twin prime is defined as a prime number that is either 2 less or 2 more than another prime number, and the difference between the two prime numbers is a multiple of 3. If no twin primes exist in the given range, the function should print a message indicating this.
"""

def print_twin_primes(start, end):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    twin_primes = []
    for num in range(start, end + 1):
        if is_prime(num) and (is_prime(num - 2) or is_prime(num + 2)) and abs(num - (num - 2)) % 3 == 0:
            twin_primes.append(num)
    if twin_primes:
        return "Twin primes between " + str(start) + " and " + str(end) + ": " + str(twin_primes)
    else:
        return "No twin primes between " + str(start) + " and " + str(end)