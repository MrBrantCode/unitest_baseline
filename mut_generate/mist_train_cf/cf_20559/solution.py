"""
QUESTION:
Create a function called `print_odd_primes` that takes a list of integers as input and prints out all the prime numbers that are odd. The function should also print the total count of prime numbers that are even in the input list. Note that prime numbers that are even are limited to 2.
"""

def print_odd_primes(lst):
    """
    Prints out all the prime numbers that are odd in the input list and prints the total count of prime numbers that are even.

    Args:
        lst (list): A list of integers.
    """
    def is_prime(num):
        """Checks if a number is prime."""
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    count_even_primes = 0
    for num in lst:
        if is_prime(num):
            if num % 2 != 0:  # check if the number is odd
                print(num)  # number is prime and odd
            else:
                count_even_primes += 1  # count prime numbers that are even

    print("Count of prime numbers that are even:", count_even_primes)