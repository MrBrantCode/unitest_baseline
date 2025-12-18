"""
QUESTION:
Implement a function named `binary_search` that takes a sorted list of integers and a target number as input, and returns `True` if the number is found in the list, and `False` otherwise. The function should have a time complexity of O(log n), where n is the length of the list.
"""

def binary_search(sorted_list, target_number):
    start = 0
    end = len(sorted_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if sorted_list[mid] == target_number:
            return True
        elif sorted_list[mid] < target_number:
            start = mid + 1
        else:
            end = mid - 1

    return False