"""
QUESTION:
Implement a function `get_even_prime_and_merge` that takes two lists of integers as input and returns a list of even prime numbers from both lists, merged and sorted in descending order. Define two helper functions: `merge_and_sort` to merge and sort the lists, and `is_prime` to check the primality of a number. The function should filter out numbers that are not prime and handle lists containing both positive and negative integers.
"""

def get_even_prime_and_merge(list1: list, list2: list):
    def merge_and_sort(m: list, n: list):
        return sorted(m + n, reverse=True)

    def is_prime(x: int):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    even_prime_numbers = [num for num in list1 + list2 if num % 2 == 0 and is_prime(abs(num))]
    return merge_and_sort(even_prime_numbers, [])