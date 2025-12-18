"""
QUESTION:
Write a function `sum_divisible_by_three_and_five` that takes a list of integers as input and returns the sum of all numbers in the list that are divisible by both 3 and 5. The function should return 0 if no numbers in the list meet this condition or if the input list is empty. Do not use built-in functions or libraries.
"""

def sum_divisible_by_three_and_five(numbers):
    if len(numbers) == 0:
        return 0

    sum = 0
    for number in numbers:
        if number % 3 == 0 and number % 5 == 0:
            sum += number
    return sum