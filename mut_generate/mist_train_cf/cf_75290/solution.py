"""
QUESTION:
Partition a list of integers into two lists, one containing even numbers and the other containing odd numbers, and sort both lists in descending order. The function should handle both positive and negative integers. 

The function should be named `partition_and_sort` and take a list of integers as an argument. It should return a list containing two lists: the first list contains even numbers in descending order and the second list contains odd numbers in descending order.
"""

def partition_and_sort(lst):
    evens = sorted([i for i in lst if i % 2 == 0], reverse=True)
    odds = sorted([i for i in lst if i % 2 != 0], reverse=True)
    return [evens, odds]