"""
QUESTION:
Write a function called `remove_elements_less_than_average` that takes a list of integers as input and removes all elements that are less than the average of all the elements in the list. The function should then return the sum of the remaining elements in the list. 

The input list should have at least 10 elements, and all elements should be integers between -100 and 100 (inclusive). The function should calculate the average without using any built-in functions or methods, and it should only use a single loop without any nested loops. The function should sort the input list in ascending order before performing any operations on it, but it should not use any additional data structures. If all elements in the input list are less than the average, the function should return 0 as the sum of the remaining elements.
"""

def remove_elements_less_than_average(lst):
    # Sort the input list in ascending order
    lst.sort()

    # Calculate the average of all the elements in the list
    total = 0
    for num in lst:
        total += num
    average = total / len(lst)

    # Remove elements that are less than the average
    i = 0
    while i < len(lst):
        if lst[i] < average:
            lst.pop(i)
        else:
            i += 1

    # Calculate the sum of the remaining elements
    total = 0
    for num in lst:
        total += num

    return total