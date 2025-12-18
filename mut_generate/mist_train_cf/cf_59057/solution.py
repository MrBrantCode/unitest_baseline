"""
QUESTION:
Write a function `calculate` that takes a list of integers as input and returns a tuple containing the maximum (apex), minimum (nadir), and mean values of the list. The function should have a time complexity of O(n) and should not use Python's built-in `max`, `min`, or `sum` functions.
"""

def calculate(numbers):
    apex = numbers[0]
    nadir = numbers[0]
    sum_of_numbers = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > apex:
            apex = numbers[i]
        elif numbers[i] < nadir:
            nadir = numbers[i]
        sum_of_numbers += numbers[i]
    mean = sum_of_numbers / len(numbers)
    return apex, nadir, mean