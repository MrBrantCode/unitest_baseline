"""
QUESTION:
Create a function named `group_by_prime` that takes a list of integers as input. The function should return a dictionary with two keys: 'positive' and 'negative'. The values for these keys should be lists of prime numbers from the input list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should consider the absolute value of each number when checking if it's prime. If a number is not prime, it should be ignored and not included in the dictionary.
"""

def group_by_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes_dict = {'positive': [], 'negative': []}
    for num in numbers:
        if is_prime(abs(num)):
            if num > 0:
                primes_dict['positive'].append(num)
            else:
                primes_dict['negative'].append(num)
    return primes_dict