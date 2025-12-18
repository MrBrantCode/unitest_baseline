"""
QUESTION:
Create a function named `complex_prime_sort` that takes two lists `l1` and `l2` as input and returns a list of even prime numbers from both lists, sorted in reverse order. Note that a prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself, and the only even prime number is 2.
"""

def complex_prime_sort(l1: list, l2: list):
    """
    Gather a sorted list of even numbers which are simultaneously prime from two listed sets.
    """

    def prime_check(x: int):
        # Confirm the primality of the integer, while note that 2 is the only even prime number
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    list_prime_even = [num for num in l1 + l2 if num % 2 == 0 and prime_check(num)]
    return sorted(list_prime_even, reverse=True)