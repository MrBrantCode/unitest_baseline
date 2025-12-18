"""
QUESTION:
Write a function `find_min_nonconsecutive_numbers` that takes a list of numbers as input and returns the minimum number of non-consecutive numbers needed to reach a sum of 150 without picking any two consecutive numbers. The function should return -1 if it's impossible to reach the sum.
"""

def find_min_nonconsecutive_numbers(numbers):
    non_consecutive_numbers = []
    previous_number = 0
    for number in numbers:
        if number - previous_number > 1:
            non_consecutive_numbers.append(number)
            previous_number = number
            if sum(non_consecutive_numbers) == 150:
                return len(non_consecutive_numbers)
    return -1