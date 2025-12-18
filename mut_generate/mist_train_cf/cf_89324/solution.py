"""
QUESTION:
Replace even numbers with their square and odd numbers with their cube in a list of integers and round each number to the nearest whole number. The function should be able to handle a list of up to 10^7 elements and have a time complexity of O(n), where n is the number of elements in the list. Implement the function `square_or_cube(arr)`, where `arr` is a list of integers.
"""

def square_or_cube(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = round(arr[i] ** 2)
        else:
            arr[i] = round(arr[i] ** 3)
    return arr