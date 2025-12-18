"""
QUESTION:
Write a function `count_numbers_greater_than_average` that takes a list of numbers as input and returns the count of numbers greater than the average of all numbers in the list. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the list.
"""

def count_numbers_greater_than_average(numbers):
    if not numbers:
        return 0

    total = sum(numbers)
    average = total / len(numbers)
    count = sum(1 for num in numbers if num > average)

    return count