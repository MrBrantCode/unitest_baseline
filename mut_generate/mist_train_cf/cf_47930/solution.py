"""
QUESTION:
Write a function named `median` that calculates the median of a list of numbers. The function should take a list of numbers as input and return the median. The median is the middle value in a sorted list of numbers. If the list has an even number of elements, the median is the average of the two middle elements. The function should also handle the case where the input list is empty, in which case it should return `None`. The function should be efficient and able to handle large input lists.
"""

def median(my_list):
    if not my_list:
        return None

    my_list.sort()
    half = len(my_list) // 2
    
    if len(my_list) % 2 == 0:
        return (my_list[half - 1] + my_list[half]) / 2
    else:
        return my_list[half]