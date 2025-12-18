"""
QUESTION:
Write a program with two functions, `is_prime(num)` and `next_prime(num)`. The `is_prime(num)` function checks if the input number `num` is a prime number, and the `next_prime(num)` function finds the next prime number after `num`. The program should then take an integer as input, check if it's prime using `is_prime(num)`, and if not, print the next prime number using `next_prime(num)`. Assume that the input number is a positive integer.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(num):
    next_num = num + 1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += 1