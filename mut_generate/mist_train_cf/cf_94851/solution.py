"""
QUESTION:
Write a function named `find_smallest_number` that takes a list of numbers as input and returns the smallest number in the list without using any built-in functions or methods in Python, such as min(), sorted(), or sort(). The list may contain negative numbers and decimals.
"""

def find_smallest_number(numbers):
    smallest = numbers[0]  # Assume the first number is the smallest
    
    for num in numbers:
        if num < smallest:
            smallest = num
    
    return smallest