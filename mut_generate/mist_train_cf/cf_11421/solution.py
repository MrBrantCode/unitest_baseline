"""
QUESTION:
Create a function `find_mean` that calculates the mean of a list of numbers. The function should iterate through the list to manually calculate the sum and length of the list, without using the built-in `sum()` or `len()` functions. The function should return the calculated mean. The input list can contain up to 1000 elements.
"""

def find_mean(numbers):
    sum_numbers = 0
    count = 0

    for num in numbers:
        sum_numbers += num
        count += 1

    mean = sum_numbers / count
    return mean