"""
QUESTION:
Write a function to generate all prime numbers between two given numbers. The function should take two parameters, start and end, which represent the range of numbers to check for primes. It should return a list of all prime numbers in the range, including the start and end numbers if they are prime. The function should be designed to work efficiently with large ranges.
"""

def entrance(start, end):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes