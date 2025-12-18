"""
QUESTION:
Write a function named `select_primes` that takes three inputs: a list of integers `test_list`, an integer `N`, and an integer `S`. The function should return two values: a list of prime numbers from `test_list` whose index is a multiple of `N` and have a digit sum greater than `S`, and the sum of these selected prime numbers.
"""

def select_primes(test_list, N, S):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    selected_primes = []
    prime_sum = 0
    for i in range(len(test_list)):
        if i % N == 0:
            number = test_list[i]
            if is_prime(number) and sum(int(digit) for digit in str(number)) > S:
                selected_primes.append(number)
                prime_sum += number
    return selected_primes, prime_sum