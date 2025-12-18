"""
QUESTION:
Write a function named `filter_and_sort` that takes a list of unique integers and a target integer within the range of the list as parameters. The function should return a new list containing the elements from the original list that are greater than the target integer, sorted in ascending order.
"""

def filter_and_sort(lst, target):
    return sorted([num for num in lst if num > target])