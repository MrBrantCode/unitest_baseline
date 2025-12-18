"""
QUESTION:
Write a function named `find_second_largest_odd_index` that takes a list of integers as input. The function should return the index of the second largest odd value in the list. If no such index exists, return -1. The list may contain both positive and negative numbers and may have duplicate values.
"""

def find_second_largest_odd_index(nums):
    largest = second_largest = float('-inf')
    largest_index = second_largest_index = -1

    for i, num in enumerate(nums):
        if num % 2 != 0:
            if num > largest:
                second_largest = largest
                second_largest_index = largest_index
                largest = num
                largest_index = i
            elif num > second_largest and num != largest:
                second_largest = num
                second_largest_index = i

    return second_largest_index