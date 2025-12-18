"""
QUESTION:
Create a function `largest_prime(lst)` that returns the largest prime number in a list. If the list contains any non-prime numbers, return "Error: List contains non-prime numbers." If the list is empty, return "Error: List is empty."
"""

def largest_prime(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_numbers = []
    for num in lst:
        if is_prime(num):
            prime_numbers.append(num)
        else:
            return "Error: List contains non-prime numbers."
    if not prime_numbers:
        return "Error: List is empty."
    else:
        return max(prime_numbers)