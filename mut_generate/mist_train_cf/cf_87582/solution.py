"""
QUESTION:
Write a function named `bubble_sort_tuples` that takes a list of tuples as input, where each tuple contains four elements. The function should sort the list of tuples in ascending order based on the third element of each tuple. If two tuples have the same third element, they should be sorted in descending order based on the first element. If two tuples have the same third and first elements, they should be sorted in ascending order based on the second element. If two tuples have the same third, first, and second elements, they should be sorted in descending order based on the fourth element. The function should have a time complexity of O(n^2) and should not use any built-in sorting functions or methods, or any additional data structures except for variables used for iteration and temporary storage.
"""

def bubble_sort_tuples(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            # Compare the third element of the tuples
            if lst[j][2] > lst[j+1][2]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            elif lst[j][2] == lst[j+1][2]:
                # Compare the first element of the tuples
                if lst[j][0] < lst[j+1][0]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                elif lst[j][0] == lst[j+1][0]:
                    # Compare the second element of the tuples
                    if lst[j][1] > lst[j+1][1]:
                        lst[j], lst[j+1] = lst[j+1], lst[j]
                    elif lst[j][1] == lst[j+1][1]:
                        # Compare the fourth element of the tuples
                        if lst[j][3] < lst[j+1][3]:
                            lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst