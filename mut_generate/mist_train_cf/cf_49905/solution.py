"""
QUESTION:
Implement a function called `bubble_sort` that takes a list of integers as input and returns the sorted list in ascending order. The function should use the bubble sort algorithm and modify the input list in-place. The input list can contain any number of elements and may be empty. The function should have a time complexity of O(n^2), where n is the number of elements in the list.
"""

def bubble_sort(numbers):
    for i in range(len(numbers)-1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers