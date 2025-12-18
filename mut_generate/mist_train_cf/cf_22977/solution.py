"""
QUESTION:
Write a function `find_max_min(numbers)` that takes a list of integers, removes duplicates from the list, and returns the maximum and minimum values in the list without using any built-in functions or methods. The function should iterate through the list only once and return `None` for both maximum and minimum values if the list is empty.
"""

def find_max_min(numbers):
    # Check if the list is empty
    if len(numbers) == 0:
        return None, None

    # Initialize max_value and min_value with the first element in the list
    max_value = numbers[0]
    min_value = numbers[0]

    # Iterate through the list to find the maximum and minimum values and remove duplicates
    unique_numbers = set()
    for num in numbers:
        if num not in unique_numbers:
            if num > max_value:
                max_value = num
            if num < min_value:
                min_value = num
            unique_numbers.add(num)

    return max_value, min_value