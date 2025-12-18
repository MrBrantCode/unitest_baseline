"""
QUESTION:
Write a function `find_second_smallest` that takes a list of integers as input and returns the second smallest element. The list will contain at least 4 unique integers in the range of -1000 to 1000.
"""

def find_second_smallest(numbers):
    smallest = min(numbers[0], numbers[1])
    second_smallest = max(numbers[0], numbers[1])
    
    for num in numbers[2:]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
            
    return second_smallest