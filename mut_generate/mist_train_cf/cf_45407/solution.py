"""
QUESTION:
Create a function called `bubble_sort` that takes one argument, a list of integers. Sort the list using the bubble sort algorithm and return the sorted list. The function should not use any extra space (space complexity O(1)) and should be able to handle lists of any size.
"""

def bubble_sort(list):
    for num in range(len(list)-1,0,-1):
        for i in range(num):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list