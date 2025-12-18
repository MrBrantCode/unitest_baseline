"""
QUESTION:
Write a function `print_prime_numbers_and_sum` that takes a string of comma-separated numbers as input, prints all the prime numbers (both positive and negative), and returns the sum of these prime numbers. The input string may contain positive and negative integers as well as floating-point numbers.
"""

import math

def print_prime_numbers_and_sum(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(abs(n))) + 1):
            if abs(n) % i == 0:
                return False
        return True

    prime_sum = 0

    num_list = numbers.split(',')
    for num in num_list:
        try:
            n = int(num)
            if is_prime(n):
                print(n)
                prime_sum += n
        except ValueError:
            pass

    print("Sum of prime numbers:", prime_sum)