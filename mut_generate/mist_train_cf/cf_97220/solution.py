"""
QUESTION:
Write a function that outputs all prime numbers between two given numbers. 

The function should accept two parameters, `start` and `end`, representing the start and end of the range (inclusive). It should return a list of all prime numbers in the range from `start` to `end`. The function should be efficient and able to handle large ranges. 

For example, for `start = 100` and `end = 1000`, the function should return a list of all prime numbers between 100 and 1000 (inclusive).
"""

def find_primes_in_range(start, end):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes