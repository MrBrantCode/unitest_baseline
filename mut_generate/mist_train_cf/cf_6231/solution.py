"""
QUESTION:
Write a function `square_or_cube` that takes a list of integers as input and returns the modified list. The function should replace even numbers with their square and odd numbers with their cube, rounding each result to the nearest whole number. The function should have a time complexity of O(n), where n is the number of elements in the list, and the list can contain up to 10^7 elements.
"""

def square_or_cube(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = round(arr[i] ** 2)
        else:
            arr[i] = round(arr[i] ** 3)
    return arr