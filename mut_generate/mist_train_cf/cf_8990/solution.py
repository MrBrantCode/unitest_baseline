"""
QUESTION:
Write a function `reorder_array(arr)` that takes an array of integers as input and returns a new array where the relative order of odd and even numbers is maintained. The function should separate the odd numbers from the even numbers and place the odd numbers first in the resulting array, followed by the even numbers. The order of odd numbers and even numbers within their respective groups should remain the same as in the original array.
"""

def reorder_array(arr):
    oddArr = []
    evenArr = []

    for num in arr:
        if num % 2 == 0:
            evenArr.append(num)
        else:
            oddArr.append(num)

    return oddArr + evenArr