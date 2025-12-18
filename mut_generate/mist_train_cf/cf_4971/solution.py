"""
QUESTION:
Find the most frequently occurring item in a sorted list of integers.

Write a function `find_most_frequent_item` that takes a sorted list of integers as input and returns the most frequently occurring item. The length of the list is n and each integer is in the range of 1 to m. The function should have a time complexity of O(n) and a space complexity of O(m). Do not use any additional data structures or built-in functions. The input list is already sorted in ascending order.
"""

def find_most_frequent_item(arr):
    if not arr:
        return None
    max_count = 0
    most_frequent = None
    count = 0
    current_item = None

    for i in range(len(arr)):
        if arr[i] == current_item:
            count += 1
        else:
            if count > max_count:
                max_count = count
                most_frequent = current_item
            current_item = arr[i]
            count = 1

    # Check if the last item in the list is the most frequent
    if count > max_count:
        max_count = count
        most_frequent = current_item

    return most_frequent