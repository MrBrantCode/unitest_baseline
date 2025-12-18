"""
QUESTION:
Delete the last three elements from a given list of integers and print the remaining elements in descending order. Implement a function named `delete_and_sort` that takes a list of integers as input and returns the sorted list. The function should modify the original list by deleting the last three elements and then sorting it in descending order.
"""

def delete_and_sort(lst):
    del lst[-3:]
    lst.sort(reverse=True)
    return lst