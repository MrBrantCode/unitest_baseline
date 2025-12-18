"""
QUESTION:
Write a function named `find_mean` that takes a list of numbers as input and returns the mean of the numbers. The function must calculate the sum and count of the numbers manually by iterating through the list using a loop, without using the `sum()` function, `len()` function, or any other built-in functions to calculate the sum or length of the list. The input list can contain up to 1000 elements.
"""

def find_mean(numbers):
    sum_numbers = 0
    count = 0

    for num in numbers:
        sum_numbers += num
        count += 1

    mean = sum_numbers / count
    return mean