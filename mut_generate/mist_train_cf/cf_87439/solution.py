"""
QUESTION:
Create a function `get_prime_numbers` that returns a list of all prime numbers between a given lower limit and upper limit. The function should achieve a time complexity of O(n * sqrt(m)), where n is the number of elements in the range and m is the average value of the range, and a space complexity of O(n), where n is the number of prime numbers in the range. The function should not use any external libraries or pre-generated lists of prime numbers, and should not use built-in functions or methods that directly check for primality.
"""

def get_prime_numbers(lower_limit, upper_limit):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for num in range(lower_limit, upper_limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes