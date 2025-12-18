"""
QUESTION:
Write a function `harmonic_mean_prime(lst)` that takes a list of integers as input and returns the harmonic mean of all prime numbers in the list. The function should return 0 if the list does not contain any prime numbers.
"""

def harmonic_mean_prime(lst):
    def check_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    prime_nums = [num for num in lst if check_prime(num)]
    if len(prime_nums) == 0:
        return 0
    sum_reciprocal = sum(1/num for num in prime_nums)
    return len(prime_nums)/sum_reciprocal