"""
QUESTION:
Write a recursive function named `print_primes` that takes two arguments, `start` and `end`, representing a range of numbers. The function should print all prime numbers within this range using a time complexity of O(n^2) without relying on built-in functions or libraries for checking prime numbers. The function should check each number in the range to determine if it is prime and print it if so.
"""

def print_primes(start, end):
    def is_prime(n, divisor):
        if n <= 2:
            return True
        if n % divisor == 0:
            return False
        if divisor * divisor > n:
            return True
        return is_prime(n, divisor + 1)

    if start > end:
        return
    
    if is_prime(start, 2):
        print(start)
    
    print_primes(start + 1, end)