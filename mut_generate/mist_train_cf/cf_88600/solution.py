"""
QUESTION:
Implement the function `find_smallest(arr)` that takes an array of integers as input and returns the smallest number in the array. The function should have a time complexity of O(n), where n is the size of the array, and use constant space complexity. The implementation must not use built-in functions, sorting, or any other optimization technique that results in a time complexity less than O(n). A single loop must be used to iterate through the array. The input array will have a length of at least 1 and at most 10^6.
"""

def find_smallest(arr):
    smallest = arr[0]  # Initialize smallest as the first element of the array

    for num in arr:
        if num < smallest:
            smallest = num  # Update smallest if the current number is smaller

    return smallest