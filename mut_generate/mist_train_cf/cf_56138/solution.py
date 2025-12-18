"""
QUESTION:
Create a function `prime_digit_sum(lst)` that takes a list of integers as input. The function should find the largest prime number in the list, then return the sum of its digits. If no prime numbers are found in the list, return 0.
"""

def prime_digit_sum(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def sum_digits(n):
        return sum(map(int, str(n)))

    prime_list = [x for x in lst if is_prime(x)]
    if not prime_list:
        return 0
    largest_prime = max(prime_list)
    return sum_digits(largest_prime)