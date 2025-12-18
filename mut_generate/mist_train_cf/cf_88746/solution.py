"""
QUESTION:
Write a function `print_prime_numbers_and_sum(numbers)` that takes a string of comma-separated integers as input, prints each prime number found in the string, and prints the sum of these prime numbers. The input string may contain both positive and negative integers.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def print_prime_numbers_and_sum(numbers):
    prime_sum = 0

    num_list = numbers.split(',')
    for num in num_list:
        try:
            n = int(num)
            if is_prime(abs(n)):
                print(n)
                prime_sum += n
        except ValueError:
            pass

    print("Sum of prime numbers:", prime_sum)