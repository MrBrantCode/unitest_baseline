"""
QUESTION:
Write a function `normalize_list` that takes a list of numbers as input and returns a new list where the sum of the numbers is 10. If the original sum is already 10, return the original list. If the original sum is less than 10, distribute the difference evenly among the elements and round to the nearest integer. If the original sum is greater than 10, proportionally reduce the values to make the sum equal to 10 and round to the nearest integer.
"""

def normalize_list(numbers):
    sum_numbers = sum(numbers)
    if sum_numbers == 10:
        return numbers
    elif sum_numbers < 10:
        remaining = 10 - sum_numbers
        distribution = remaining / len(numbers)
        return [round(num + distribution) for num in numbers]
    else:
        reduction_ratio = 10 / sum_numbers
        return [round(num * reduction_ratio) for num in numbers]