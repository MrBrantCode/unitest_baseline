"""
QUESTION:
Given a list of numbers from 1 to n and a target sum, write a function `find_min_nonconsecutive_numbers` that returns the minimum number of non-consecutive numbers needed to reach the target sum without picking any two consecutive numbers. If it's impossible to reach the sum, return -1.
"""

def find_min_nonconsecutive_numbers(numbers, target_sum):
    non_consecutive_numbers = []
    previous_number = 0
    for number in numbers:
        if number - previous_number > 1:
            non_consecutive_numbers.append(number)
            previous_number = number
            if sum(non_consecutive_numbers) == target_sum:
                return len(non_consecutive_numbers)
    return -1