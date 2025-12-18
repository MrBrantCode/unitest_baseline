"""
QUESTION:
Create a function named `print_last_n_unique_primes` that takes a list of integers and an integer `n` as input. The function should print the last `n` unique prime numbers from the list, excluding any duplicates. If the list has fewer than `n` unique prime numbers, it should print all the unique prime numbers in the list without duplicates. The function should have a time complexity of O(n^2) and a space complexity of O(n).
"""

def print_last_n_unique_primes(lst, n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    unique_primes = []
    for num in lst:
        if is_prime(num) and num not in unique_primes:
            unique_primes.append(num)

    if len(unique_primes) <= n:
        print(unique_primes)
    else:
        print(unique_primes[-n:])