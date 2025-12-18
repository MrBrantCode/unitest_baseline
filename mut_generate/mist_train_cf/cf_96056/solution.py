"""
QUESTION:
Write a function `print_first_n_even_numbers(n)` that prints the first `n` even numbers that are multiples of 4, greater than 100, and have a digit sum that is a prime number.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_digits_is_prime(n):
    digit_sum = sum(int(d) for d in str(n))
    return is_prime(digit_sum)

def print_first_n_even_numbers(n):
    count = 0
    number = 100
    while count < n:
        if number % 2 == 0 and number % 4 == 0 and sum_of_digits_is_prime(number):
            print(number)
            count += 1
        number += 4