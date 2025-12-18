"""
QUESTION:
Create a function `get_positive_and_sort` that takes a list of integers as input, filters out only the positive numbers, and returns them in ascending order without using built-in sorting functions. The function should implement a custom sorting technique, such as bubble sort, using a helper function `swap_elements` to swap elements in the list.
"""

def get_positive_and_sort(l: list):
    def swap_elements(n: list, index1: int, index2: int):
        n[index1], n[index2] = n[index2], n[index1]

    l = [num for num in l if num > 0]
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                swap_elements(l, j, j+1)
    return l