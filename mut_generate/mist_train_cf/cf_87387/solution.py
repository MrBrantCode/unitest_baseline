"""
QUESTION:
Write a function `select_primes` that takes a list of integers `test_list`, an integer `N`, and an integer `S` as inputs. The function should return a tuple containing a list of prime numbers and their sum. The function should only consider numbers in `test_list` whose index is a multiple of `N` and whose digit sum is greater than `S`.
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