"""
QUESTION:
Write a function `find_max_min_avg` that takes an array of numbers as input and returns the maximum, minimum, and average values without using any built-in functions or methods for sorting or finding maximum, minimum, or average. The function should have a time complexity of O(n), where n is the length of the input array, and use constant space. If the input array is empty, the function should return `None` for all three values.
"""

def find_max_min_avg(numbers):
    if len(numbers) == 0:
        return None, None, None

    max_value = float('-inf')
    min_value = float('inf')
    sum_value = 0

    for num in numbers:
        if num > max_value:
            max_value = num

        if num < min_value:
            min_value = num

        sum_value += num

    average_value = sum_value / len(numbers)
    return max_value, min_value, average_value