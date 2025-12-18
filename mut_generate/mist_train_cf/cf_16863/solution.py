"""
QUESTION:
Implement a function called `bubble_sort` that takes a list of integers as input and returns the list sorted in ascending order using the Bubble Sort algorithm. The input list will not exceed 1000 in length and will contain integers in the range of -1000 to 1000, inclusive. The function should not modify the original list, but instead create a new sorted list. The time complexity of the function should be O(n^2), where n is the length of the list.
"""

def bubble_sort(lst):
    # Create a new list to store the sorted elements
    sorted_lst = list(lst)

    # Iterate through the list multiple times
    for i in range(len(sorted_lst)):
        # Each iteration moves the largest unsorted element to the end
        for j in range(len(sorted_lst) - 1):
            # Compare adjacent elements and swap them if they are in the wrong order
            if sorted_lst[j] > sorted_lst[j + 1]:
                sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
    
    # Return the sorted list
    return sorted_lst