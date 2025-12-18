"""
QUESTION:
Write a function `sum_of_primes` that calculates the sum of all prime numbers in the given array that are multiples of the given number and are greater than or equal to a specified value. The function should take three parameters: `numbers`, an array of integers; `num`, the number to check for multiples; and `min_value`, the minimum value the prime numbers should be greater than or equal to. The function should return the sum of all such prime numbers.
"""

def sum_of_primes(numbers, num, min_value):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    total_sum = 0
    for n in numbers:
        if n % num == 0 and n >= min_value and is_prime(n):
            total_sum += n
    return total_sum