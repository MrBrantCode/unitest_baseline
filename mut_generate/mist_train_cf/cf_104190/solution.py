"""
QUESTION:
Write a function called `partition_numbers` that takes a list of numbers as input and returns a tuple containing three lists: numbers divisible by 3, numbers divisible by 5, and numbers divisible by 7. The function should categorize each number in the input list into one or more of these groups based on divisibility.
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