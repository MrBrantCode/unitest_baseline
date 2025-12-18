"""
QUESTION:
Write a function `nth_prime(n)` that prints the nth prime number in ascending order, where n is a given positive integer. The function should use constant space (O(1) space complexity) and return the nth prime number.
"""

def nth_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2
        return True

    count = 0
    number = 2
    while count < n:
        if is_prime(number):
            count += 1
            if count == n:
                return number
        number += 1
    return -1