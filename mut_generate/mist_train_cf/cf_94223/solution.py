"""
QUESTION:
Design a function called `partition_numbers` that takes a list of numbers as input and returns a tuple of three lists. The function should partition the input list into numbers that are divisible by 3, numbers that are divisible by 5, and numbers that are divisible by 7. Note that a number may be divisible by more than one of these values and should be included in all applicable lists.
"""

def partition_numbers(numbers):
    divisible_by_3 = []
    divisible_by_5 = []
    divisible_by_7 = []

    for num in numbers:
        if num % 3 == 0:
            divisible_by_3.append(num)
        if num % 5 == 0:
            divisible_by_5.append(num)
        if num % 7 == 0:
            divisible_by_7.append(num)

    return (divisible_by_3, divisible_by_5, divisible_by_7)