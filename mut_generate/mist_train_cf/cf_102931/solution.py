"""
QUESTION:
Write a function named `sort_numbers` that takes a list of numbers as input and returns the sorted list in ascending order using a recursive approach. The function should handle lists of any length, including empty lists and lists with one element.
"""

def sort_numbers(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    lesser_nums = [x for x in numbers[1:] if x <= pivot]
    greater_nums = [x for x in numbers[1:] if x > pivot]
    return sort_numbers(lesser_nums) + [pivot] + sort_numbers(greater_nums)