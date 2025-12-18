"""
QUESTION:
Write a function `find_smallest_number(numbers)` that takes a list of numbers as input and returns the smallest number in the list. The list can contain negative numbers and decimals. You cannot use built-in functions or methods like min(), sorted(), or sort().
"""

def find_smallest_number(numbers):
    smallest = numbers[0]  # Assume the first number is the smallest
    
    for num in numbers:
        if num < smallest:
            smallest = num
    
    return smallest