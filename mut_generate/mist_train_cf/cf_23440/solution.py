"""
QUESTION:
Implement a function called `bubble_sort` that sorts a given list of integers in ascending order using the bubble sort algorithm. The function should take a list of integers as input and return the sorted list.
"""

def bubble_sort(list):
    swap = True
    while swap:
        swap = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
                swap = True
    return list