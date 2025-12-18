"""
QUESTION:
Write a function `find_second_smallest` that takes a list of integers as input and returns the second smallest number in the list. The function should not use any built-in sorting functions or libraries, have a time complexity of O(n), and use constant space. If the list has less than 2 distinct elements, the function should return None.
"""

def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None

    smallest = float('inf')
    second_smallest = float('inf')

    for num in my_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    if second_smallest == float('inf'):
        return None

    return second_smallest