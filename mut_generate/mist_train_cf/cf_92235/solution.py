"""
QUESTION:
Design a function named `find_primes_with_digit_sum` that takes an integer `n` as input and finds all prime numbers up to `n`. For each prime number found, calculate the sum of its digits and return or print the prime number along with the sum of its digits. Assume that the input `n` is a positive integer greater than 1.
"""

def find_primes_with_digit_sum(n):
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

    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))

    for num in range(2, n + 1):
        if is_prime(num):
            print(f"Prime number: {num}, Sum of digits: {sum_of_digits(num)}")