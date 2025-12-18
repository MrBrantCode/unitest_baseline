"""
QUESTION:
Write a function named `calculate_sum` that calculates the sum of all elements in a given list. The function should have a time complexity less than O(n^2) and a space complexity of O(1) or O(log n), where n is the number of elements in the input list.
"""

def calculate_sum(lst):
    total_sum = 0

    for num in lst:
        total_sum += num

    return total_sum