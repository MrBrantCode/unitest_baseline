"""
QUESTION:
Implement a function `find_smallest_number` that takes a list of numbers as input and returns the smallest number in the list. The function should not use any built-in functions or methods, such as min(), sorted(), or sort(), and should have a time complexity of O(n), where n is the length of the list. The input list may contain negative numbers, decimals, and duplicates.
"""

def find_smallest_number(numbers):
    smallest = float('inf')
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest