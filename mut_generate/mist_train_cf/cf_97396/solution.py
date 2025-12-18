"""
QUESTION:
Create a function `largest_prime_in_string` that takes a string as input and returns the largest prime number found in the string. The prime numbers in the string are single-digit numbers. If no prime number is found in the string, the function should return `None`. The function should only consider single-digit numbers in the string and ignore non-digit characters.
"""

def largest_prime_in_string(s):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest_prime = None
    for char in s:
        if char.isdigit():
            num = int(char)
            if is_prime(num):
                if largest_prime is None or num > largest_prime:
                    largest_prime = num
    return largest_prime