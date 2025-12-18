"""
QUESTION:
Implement a function named `bubble_sort` that takes a list of integers as input and returns a sorted list in ascending order using the Bubble Sort algorithm. The function should have a time complexity of O(n^2) and a space complexity of O(1), where n is the number of elements in the input list.
"""

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst