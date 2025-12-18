"""
QUESTION:
Write a function called `find_smallest` that finds the smallest number in an array of numbers. The function should not use any built-in functions or methods, have a time complexity of O(n), handle negative numbers, handle arrays with duplicate numbers, and not modify the original array.
"""

def find_smallest(arr):
    # Initialize the smallest number as the first element in the array
    smallest = arr[0]
    
    # Iterate through the rest of the elements in the array
    for num in arr[1:]:
        # If the current number is smaller than the smallest number,
        # update the smallest number
        if num < smallest:
            smallest = num
    
    return smallest