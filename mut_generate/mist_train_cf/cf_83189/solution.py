"""
QUESTION:
Design a function `bubble_sort_2d_array` that takes a 2D array of integers as input. The function should first sort each row of the array in ascending order using the bubble sort algorithm, and then reorder the rows in ascending order based on their sums. Return the sorted 2D array.
"""

def bubble_sort_2d_array(arr):
    # Bubble sort each row
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(len(arr[i])-j-1):
                if arr[i][k] > arr[i][k+1]:
                    arr[i][k], arr[i][k+1] = arr[i][k+1], arr[i][k]    

    # Calculate sum of each row and pair it with its index
    sum_rows = [(sum(arr[i]), i) for i in range(len(arr))]

    # Sort pairs by sum of rows
    sum_rows.sort()

    # Reorder rows in ascending order of their sums
    arr = [arr[i] for _, i in sum_rows]

    return arr