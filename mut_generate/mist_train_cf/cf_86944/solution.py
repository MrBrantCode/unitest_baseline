"""
QUESTION:
Create a function named `filter_and_sort` that takes a list of integers as input. The function should filter out all numbers divisible by 3 or 4, and then sort the remaining numbers in descending order. The function should return the sorted list of numbers.
"""

def filter_and_sort(numbers):
    filtered_numbers = []
    for num in numbers:
        if num % 3 != 0 and num % 4 != 0:
            filtered_numbers.append(num)
    
    filtered_numbers.sort(reverse=True)
    return filtered_numbers