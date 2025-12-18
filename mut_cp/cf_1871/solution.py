"""
ORIGINAL QUESTION:
Implement a function `find_median` that takes a list of numbers as input and returns the median value of the list. The list should be sorted in ascending order without using any built-in sorting functions or libraries. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements.
"""

def find_median(lst):
    n = len(lst)
    sorted_lst = bubble_sort(lst)  # Sort the list using bubble sort

    if n % 2 == 1:  # Odd number of elements
        median = sorted_lst[n // 2]
    else:  # Even number of elements
        median = (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2

    return median


def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst