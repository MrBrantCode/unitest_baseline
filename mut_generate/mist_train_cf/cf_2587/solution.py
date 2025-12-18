"""
QUESTION:
Implement a function `remove_elements_less_than_average` that takes a list of integers as input, removes all elements that are less than the average of all elements in the list, and returns the sum of the remaining elements. The function should have a time complexity of O(n), where n is the length of the input list, and should use only a single loop without nested loops or additional data structures. The function should also handle the case where all elements in the input list are less than the average. The input list should have at least 10 elements and the elements should be integers.
"""

def remove_elements_less_than_average(lst):
    # Calculate the sum of all the elements in the list
    total = sum(lst)

    # Calculate the average of all the elements in the list
    average = total / len(lst)

    # Remove elements that are less than the average and calculate the sum of the remaining elements
    remaining_sum = sum(num for num in lst if num >= average)

    return remaining_sum