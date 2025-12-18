"""
QUESTION:
Create a function `bubble_sort` that takes a list of integers as input, uses the Bubble Sort strategy to sort the list in ascending order, and returns the sorted list. The input list is not guaranteed to be of any specific length.
"""

def bubble_sort(list_to_sort):
    num_of_elements = len(list_to_sort)
    for i in range(num_of_elements):
        for j in range(0, num_of_elements - i - 1):
            # Check if current element is greater than next
            if list_to_sort[j] > list_to_sort[j + 1] :
                # Swap the elements
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
    return list_to_sort