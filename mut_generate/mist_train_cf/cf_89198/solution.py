"""
QUESTION:
Create a function `prime_numbers` that takes a list of integers as input and returns a tuple. The first element of the tuple should be a list of all prime numbers from the input list, sorted in descending order. The second element of the tuple should be the sum of all prime numbers in the input list. If there are no prime numbers in the list, the function should return a tuple containing an empty list and 0.
"""

def prime_numbers(list_of_numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_list = [num for num in list_of_numbers if is_prime(num)]
    sum_of_primes = sum(prime_list)
    return (sorted(prime_list, reverse=True), sum_of_primes)