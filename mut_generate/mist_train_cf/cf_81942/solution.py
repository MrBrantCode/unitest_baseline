"""
QUESTION:
Implement a function `bubble_sort(num_list)` that takes a list of numerical data as input, including negative and fractional numbers, and returns the sorted list in ascending order using the Bubble sort methodology.
"""

def bubble_sort(num_list):
    n = len(num_list)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if num_list[j] > num_list[j+1] :
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                swapped = True
        if swapped == False:
            break
    return num_list