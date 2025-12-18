"""
QUESTION:
Write a function `sum_odd_multiples(numbers, num, min_value)` that calculates the sum of all odd numbers in the given list `numbers` that are multiples of the given number `num` and are greater than or equal to the specified value `min_value`.
"""

def sum_odd_multiples(numbers, num, min_value):
    sum_odd = 0
    for number in numbers:
        if number % 2 != 0 and number % num == 0 and number >= min_value:
            sum_odd += number
    return sum_odd