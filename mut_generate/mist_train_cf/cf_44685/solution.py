"""
QUESTION:
Implement a function named `custom_sort` that takes a list of lists of integers as input and returns a new list where the inner lists are sorted based on the following rules:

- First, sort the inner lists based on the sum of their elements in descending order.
- If some inner lists have equal sums, then sort these inner lists by the second element in descending order.

The function should only use basic Python functionalities and should not use the in-built `sort()` or `sorted()` functions.
"""

def custom_sort(lists):
    # adding sums of elements in each list with the corresponding list
    sum_list = [[sum(lst), lst] for lst in lists]

    # Bubble sort
    n = len(sum_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (sum_list[j][0] < sum_list[j + 1][0]) or \
               (sum_list[j][0] == sum_list[j + 1][0] and sum_list[j][1][1] < sum_list[j + 1][1][1]):
                sum_list[j], sum_list[j + 1] = sum_list[j + 1], sum_list[j]

    # extracting the sorted list
    return [item[1] for item in sum_list]