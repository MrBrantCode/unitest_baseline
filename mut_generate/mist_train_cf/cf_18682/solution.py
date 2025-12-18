"""
QUESTION:
Write a function `find_nth_prime(n)` that uses a while loop to find the nth prime number without using any built-in prime number checking functions or libraries. The function should only return the nth prime number.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_nth_prime(n):
    count = 0
    number = 2
    while count < n:
        if is_prime(number):
            count += 1
        number += 1
    return number - 1