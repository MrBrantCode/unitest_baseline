"""
QUESTION:
Implement a function named `bubble_sort` that takes a list of numbers as input and returns a new list where the numbers are sorted in ascending order using the Bubble Sort algorithm. The function should only use the provided list and not any built-in sorting functions or libraries.
"""

def bubble_sort(array):
    n = len(array)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already sorted
        for j in range(0, n - i - 1):

            # Traverse the array and swap if the element found is greater
            # then the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array