"""
QUESTION:
Create a function named `get_median` that takes a list of numbers as input and returns the median value. The median is the middle value of a sorted list. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements.
"""

def get_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    middle_index = length // 2
    
    if length % 2 == 0:
        median = (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2
    else:
        median = sorted_numbers[middle_index]
        
    return median