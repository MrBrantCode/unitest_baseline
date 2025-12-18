"""
QUESTION:
Write a function `solve(lst)` that takes a list of integers as input. The function should return the sum of the digits of the largest prime number in the list. If no prime numbers are found in the list, the function's behavior is undefined. The input list may contain duplicate numbers and may be unsorted.
"""

def solve(lst):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def sum_digits(n):
        return sum(int(digit) for digit in str(n))

    max_prime = max((num for num in lst if is_prime(num)), default=0)
    return sum_digits(max_prime)