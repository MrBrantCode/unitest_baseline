"""
QUESTION:
Create a function named `find_min_max` that takes a list of integers as input and returns the smallest, largest, second smallest, and second largest numbers from the list without using any built-in functions or libraries for finding the minimum and maximum values. Assume that the input list contains at least two distinct elements.
"""

def find_min_max(lst):
    smallest = lst[0]
    largest = lst[0]

    for num in lst:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    second_smallest = None
    second_largest = None

    for num in lst:
        if num == smallest or num == largest:
            continue
        if second_smallest is None or num < second_smallest:
            second_smallest = num
        if second_largest is None or num > second_largest:
            second_largest = num

    return smallest, largest, second_smallest, second_largest