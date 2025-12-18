"""
QUESTION:
Write a function named `count_numbers_greater_than_average` that takes a list of numbers as input and returns the count of numbers greater than the average of all numbers in the list. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the list.
"""

def count_numbers_greater_than_average(numbers):
    if not numbers:
        return 0

    total = 0
    count = 0

    for num in numbers:
        total += num

    average = total / len(numbers)

    for num in numbers:
        if num > average:
            count += 1

    return count