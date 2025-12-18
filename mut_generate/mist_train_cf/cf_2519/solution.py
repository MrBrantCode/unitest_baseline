"""
QUESTION:
Implement the `non_increasing_sort` function, which takes a list of integers as input and returns the sorted list in non-increasing order. The function should have a time complexity of O(n^2) and should not use any additional data structures, built-in sorting functions, libraries, recursion, or nested loops.
"""

def non_increasing_sort(lst):
    for i in range(len(lst)):
        max_index = i
        for j in range(i+1, len(lst)):
            if lst[j] > lst[max_index]:
                max_index = j
        lst[i], lst[max_index] = lst[max_index], lst[i]
    return lst