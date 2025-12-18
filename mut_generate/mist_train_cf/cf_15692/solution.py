"""
QUESTION:
Write a function `find_max_min_avg` that takes an array of numbers as input and returns the maximum, minimum, and average values without using any built-in functions or methods to sort or find these values. The function should have a time complexity of O(n), where n is the length of the input array, and use constant space. The function should also only use functional programming concepts and higher-order functions, without any loops or recursion.
"""

from functools import reduce

def find_max_min_avg(numbers):
    max_value = float('-inf')
    min_value = float('inf')
    sum_value = 0

    def update_max(current_max, element):
        return max(current_max, element)

    def update_min(current_min, element):
        return min(current_min, element)

    def calculate_sum(current_sum, element):
        return current_sum + element

    max_value = reduce(update_max, numbers, max_value)
    min_value = reduce(update_min, numbers, min_value)
    sum_value = reduce(calculate_sum, numbers, sum_value)
    avg_value = sum_value / len(numbers)

    return max_value, min_value, avg_value