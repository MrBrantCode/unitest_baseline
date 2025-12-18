"""
QUESTION:
Create a function called `add_numbers_excluding_divisible_by_three` that takes a list of numbers as input. The function should return the sum of all numbers in the list that are not divisible by 3.
"""

def add_numbers_excluding_divisible_by_three(numbers):
    sum = 0
    for num in numbers:
        if num % 3 == 0:
            continue
        sum += num
    return sum