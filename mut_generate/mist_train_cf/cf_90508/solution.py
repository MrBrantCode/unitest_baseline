"""
QUESTION:
Write a function `bubble_sort` that sorts a list of integers in both ascending and descending order without using built-in sorting functions. The function should have a time complexity of O(n^2) and use a bubble sort algorithm. The function should also return the number of comparisons made during the sorting process. The function should be able to handle duplicate values in the list and should return two lists: one sorted in ascending order and one in descending order, along with the number of comparisons made for each.
"""

def bubble_sort(lst, asc=True):
    comparisons = 0
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comparisons += 1
            if (asc and lst[j] > lst[j+1]) or (not asc and lst[j] < lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst, comparisons