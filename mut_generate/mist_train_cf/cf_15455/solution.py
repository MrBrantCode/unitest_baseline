"""
QUESTION:
Filter the provided array by returning only prime numbers and then sort the resulting array in descending order. Write a function named `filter_and_sort_primes` that takes one parameter: an array of integers.
"""

def filter_and_sort_primes(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = [num for num in numbers if is_prime(num)]
    prime_numbers.sort(reverse=True)
    return prime_numbers