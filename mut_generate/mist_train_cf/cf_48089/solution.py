"""
QUESTION:
Implement a function `bubble_sort` that sorts a given list of lists in descending order using the Bubble sort technique. The sorting should be based on the sum of integers in each sub-list. The input and output should be lists of lists of integers.
"""

def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        for j in range(0, n - i - 1):

            if sum(lst[j]) < sum(lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst