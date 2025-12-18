"""
QUESTION:
Create a function called `sort_list_descending` that takes a list of integers as input. The function should sort the list in descending order without using any built-in sorting functions and remove any duplicate values from the sorted list. The function should return the sorted list of unique integers.
"""

def sort_list_descending(unsorted_list):
    # Remove duplicates
    unique_list = []
    for num in unsorted_list:
        if num not in unique_list:
            unique_list.append(num)

    # Sort the list in descending order using bubble sort algorithm
    n = len(unique_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if unique_list[j] < unique_list[j+1]:
                unique_list[j], unique_list[j+1] = unique_list[j+1], unique_list[j]

    return unique_list