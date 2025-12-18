"""
QUESTION:
Implement the function `sort_array` that sorts an array in ascending order using a custom sorting algorithm. The function should take an array of integers as input and return the sorted array. The function should use two nested iterations to compare and swap elements in the array. The outer iteration should iterate from the first element to the second last element, and the inner iteration should iterate from the next element of the outer iteration to the last element. If an element in the outer iteration is greater than an element in the inner iteration, the elements should be swapped. The function should repeat the iterations until all elements are sorted in ascending order.
"""

def sort_array(array):
    n = len(array)
    for i in range(n-1):
        for j in range(i+1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array