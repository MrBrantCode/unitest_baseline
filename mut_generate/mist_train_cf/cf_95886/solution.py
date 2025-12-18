"""
QUESTION:
Write a function `find_prime_sum_and_product` that takes a start and end range as input and returns the sum and product of all prime numbers within this range that are not divisible by 5. The function should not take any other parameters. The range is inclusive of the start and exclusive of the end.
"""

def find_prime_sum_and_product(start, end):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    prime_product = 1

    for num in range(start, end):
        if num % 5 == 0:
            continue
        if is_prime(num):
            prime_sum += num
            prime_product *= num
    return prime_sum, prime_product