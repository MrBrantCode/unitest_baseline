"""
QUESTION:
Write a function `sum_divisible_by_three_and_five` that takes a list of integers as input and returns the sum of all numbers in the list that are divisible by both 3 and 5. The function should return 0 if no such numbers exist.
"""

def sum_divisible_by_three_and_five(numbers):
    sum = 0
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            sum += num
    return sum