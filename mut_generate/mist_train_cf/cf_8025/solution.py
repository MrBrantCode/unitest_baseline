"""
QUESTION:
Write a function named `find_second_max` that takes an array of numbers as input and returns the second maximum value from the array. You are not allowed to use any built-in functions or methods that directly find the maximum value or sort the array. Assume the input array has at least two distinct elements.
"""

def find_second_max(numbers):
    max_value = numbers[0]
    second_max_value = float('-inf')

    for i in range(1, len(numbers)):
        if numbers[i] > max_value:
            second_max_value = max_value
            max_value = numbers[i]
        elif numbers[i] > second_max_value and numbers[i] != max_value:
            second_max_value = numbers[i]

    return second_max_value