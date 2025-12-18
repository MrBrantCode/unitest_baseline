"""
QUESTION:
Design a function `reversed_and_sum` that takes a list of integers as input, reverses the list, and returns the reversed list along with the sum of all prime numbers in the reversed list. The function should work with dynamic lists and handle edge cases such as empty lists, lists with all prime numbers, lists with no prime numbers, and lists with negative numbers.
"""

def is_prime(n):
    """check if a number is Prime"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def reversed_and_sum(my_list):
    """Return reversed list and sum of primes in the list"""
    my_list = my_list[::-1]
    sum_primes = sum(i for i in my_list if is_prime(i))
    return my_list, sum_primes