"""
QUESTION:
Write a function `print_reverse_primes` that takes a list of integers as input and prints the prime numbers from the list in reverse order, while optimizing the time complexity of the solution. The function should not return any value, it should only print the prime numbers. The input list can contain duplicate numbers, and the function should print each prime number only once.
"""

def print_reverse_primes(arr):
    def is_prime(n):
        if n < 2:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        else:
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

    prime_numbers = set()

    for x in reversed(arr):
        if is_prime(x):
            prime_numbers.add(x)

    for prime_number in reversed(sorted(prime_numbers)):
        print(prime_number)