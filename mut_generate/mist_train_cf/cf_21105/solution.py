"""
QUESTION:
Create a function named `sum_even_not_divisible_by_3` that takes a list of integers as input. The function should return the sum of all even numbers in the list that are not divisible by 3. If there are no such numbers, the function should return -1. The input list can contain negative numbers.
"""

def sum_even_not_divisible_by_3(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0 and num % 3 != 0]
    return sum(even_numbers) if even_numbers else -1