"""
QUESTION:
Write a function `calculate_sum(lst)` that calculates the sum of all elements in the given list `lst`. The time complexity should be less than O(n^2) and the space complexity should be O(1) or O(log n), where n is the number of elements in the input list.
"""

def entrance(lst):
    total_sum = 0

    for num in lst:
        total_sum += num

    return total_sum