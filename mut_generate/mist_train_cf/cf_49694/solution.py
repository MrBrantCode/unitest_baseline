"""
QUESTION:
Write a Python function named `print_primes(max_n)` that prints all prime numbers less than or equal to `max_n`. The function should handle cases where `max_n` is not a positive integer or exceeds 10000. The input `max_n` will be provided by the user and is expected to be an integer. Implement the function to optimize its time complexity.
"""

def print_primes(max_n):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = int(n**0.5) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True

    if not isinstance(max_n, int) or max_n < 1:
        print("Please enter a positive integer.")
        return
    if max_n > 10000:
        print("Input exceeds the threshold, please input a smaller number.")
        return
    n = 2
    while n <= max_n:
        if is_prime(n):
            print(n)
        n += 1