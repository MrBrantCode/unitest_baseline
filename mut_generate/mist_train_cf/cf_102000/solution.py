"""
QUESTION:
Write a function called `filter_and_sort` that takes two parameters: a list of distinct integers and a target integer within the range of the list. The function should return a new list containing only the elements from the original list that are greater than the target integer, sorted in ascending order.
"""

def filter_and_sort(lst, target):
    filtered_lst = [num for num in lst if num > target]
    sorted_lst = sorted(filtered_lst)
    return sorted_lst