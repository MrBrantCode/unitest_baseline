"""
QUESTION:
Write a program that implements the bubble sort algorithm to sort a list of integers in both ascending and descending order without using any built-in sorting functions. The program should return the sorted list and the number of comparisons made during the sorting process. The time complexity of the program should be O(n^2). The program should handle duplicate values in the list and should use additional data structures if necessary.
"""

def bubble_sort(lst, order="asc"):
    comparisons = 0
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comparisons += 1
            if (order == "asc" and lst[j] > lst[j+1]) or (order == "desc" and lst[j] < lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst, comparisons