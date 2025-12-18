"""
QUESTION:
Write a function named 'find_second_largest' that takes an array of integers 'numbers' with at least 2 unique elements and returns the second largest element in the array. The function should have a time complexity of O(n) and cannot use any built-in sorting functions or methods. If the array has less than 2 unique elements, the function should return None.
"""

def find_second_largest(numbers):
    if len(numbers) < 2:
        return None
    max_value = float('-inf')
    second_max_value = float('-inf')
    for num in numbers:
        if num > max_value:
            second_max_value = max_value
            max_value = num
        elif num > second_max_value and num != max_value:
            second_max_value = num
    return second_max_value if second_max_value != float('-inf') else None