"""
QUESTION:
Write a function called `find_min_max` that takes a list of integers as input and returns the smallest, largest, second smallest, and second largest numbers from the list. The function should not use any built-in functions or libraries for finding the minimum and maximum values.
"""

def find_min_max(lst):
    # Initialize variables for smallest and largest numbers
    smallest = lst[0]
    largest = lst[0]

    # Iterate through the list and update smallest and largest variables
    for num in lst:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    # Initialize variables for second smallest and second largest numbers
    second_smallest = None
    second_largest = None

    # Iterate through the list again and update second_smallest and second_largest variables
    for num in lst:
        # Skip the smallest and largest numbers
        if num == smallest or num == largest:
            continue
        if second_smallest is None or num < second_smallest:
            second_smallest = num
        if second_largest is None or num > second_largest:
            second_largest = num

    return smallest, largest, second_smallest, second_largest