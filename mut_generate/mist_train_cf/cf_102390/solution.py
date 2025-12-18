"""
QUESTION:
Write a function `find_average(numbers)` that calculates the average of a list of numbers. The function should only calculate the average if the list contains at least one positive number. If the list does not contain any positive numbers, return 0. Additionally, the function should handle the case when the input is not a list and return an error message "Error: Invalid input."
"""

def find_average(numbers):
    if not isinstance(numbers, list):
        return "Error: Invalid input."
    sum = 0
    count = 0
    positive_count = 0
    for num in numbers:
        sum += num
        count += 1
        if num > 0:
            positive_count += 1
    if positive_count > 0:
        return sum / count
    else:
        return 0