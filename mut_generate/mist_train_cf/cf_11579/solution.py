"""
QUESTION:
Write a function `prime_digit_sum` that takes two integers `start` and `end` as input and returns the sum of the digits of all prime numbers in the range from `start` to `end` (inclusive). The function should consider a prime number as a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def prime_digit_sum(start, end):
    """
    This function calculates the sum of the digits of all prime numbers 
    in the range from start to end (inclusive).
    
    Args:
        start (int): The start of the range (inclusive).
        end (int): The end of the range (inclusive).
    
    Returns:
        int: The sum of the digits of all prime numbers in the range.
    """
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sum_of_digits(n):
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total

    total_sum = 0
    for num in range(start, end + 1):
        if is_prime(num):
            total_sum += sum_of_digits(num)
    return total_sum