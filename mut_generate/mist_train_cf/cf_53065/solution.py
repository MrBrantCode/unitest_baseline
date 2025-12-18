"""
QUESTION:
Implement a function `bubble_sort(list)` that sorts an array of integers in ascending order without using any built-in sorting procedures. The function should return the sorted list. The input list contains only integers and may be empty or contain duplicate values.
"""

def entrance(list):
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]
    return list