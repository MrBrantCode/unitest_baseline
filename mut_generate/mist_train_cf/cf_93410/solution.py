"""
QUESTION:
Write a function `calculate_sum_and_average` that takes a list of numbers as input and returns a tuple containing the sum and average of the numbers in the list. The function must use a for loop to calculate the sum.
"""

def calculate_sum_and_average(numbers):
    sum_of_numbers = 0
    for num in numbers:
        sum_of_numbers += num
    average = sum_of_numbers / len(numbers)
    return sum_of_numbers, average