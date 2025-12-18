"""
QUESTION:
Write a function `sum_of_squares_prime_numbers` that takes a list of integers as input and returns the sum of the squares of all prime numbers in the list, excluding numbers that are divisible by both 3 and 5. The function should have a time complexity of O(n), where n is the length of the input list, and a space complexity of O(1).
"""

from typing import List

def sum_of_squares_prime_numbers(numbers: List[int]) -> int:
    def is_prime(number: int) -> bool:
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    sum_of_squares = 0
    for number in numbers:
        if is_prime(number) and number % 3 != 0 and number % 5 != 0:
            sum_of_squares += number ** 2

    return sum_of_squares