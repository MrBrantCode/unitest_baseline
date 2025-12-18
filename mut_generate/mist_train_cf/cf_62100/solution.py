"""
QUESTION:
Implement the `bubble_sort` function to sort a list of numbers in ascending order using the bubble sort algorithm, working strictly in-place without using any auxiliary data structures or built-in sorting functions. The function should modify the original list and return it.
"""

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j+1]:      # If current element is greater than next
                list[j], list[j+1] = list[j+1], list[j]      # Swap the elements
    return list