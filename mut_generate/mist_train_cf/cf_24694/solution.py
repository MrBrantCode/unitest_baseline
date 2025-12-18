"""
QUESTION:
Write a function `find_largest_number` that takes a list of numbers as input and returns the largest number. The function should iterate through the list to find the maximum value.
"""

def find_largest_number(numbers):
    largest_number = numbers[0]
    for num in numbers[1:]:
        if num > largest_number:
            largest_number = num
    return largest_number