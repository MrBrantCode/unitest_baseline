"""
QUESTION:
Create a function called `filter_and_sort_numbers` that takes a list of numbers as input. The function should filter out the numbers that are greater than 100 and less than 1000, then return the remaining numbers sorted in descending order. The length of the list can be up to 10^6, the time complexity of the solution should be O(n log n), and the space complexity should be O(n), where n is the length of the list.
"""

def filter_and_sort_numbers(numbers):
    filtered_numbers = [num for num in numbers if num > 100 and num < 1000]
    return sorted(filtered_numbers, reverse=True)