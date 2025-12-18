"""
QUESTION:
Write a function called `find_sum_average_max_min` that takes an array of integers as input. Using a single loop, calculate the sum of all elements, the average of the sum, the maximum element, and the minimum element in the array. The function should return these four values. Assume the input array is not empty, but handle the case where the input array is empty. The time complexity of the solution must be O(n), where n is the length of the input array. Do not use any built-in array methods or functions.
"""

def find_sum_average_max_min(arr):
    n = len(arr)
    if n == 0:
        return None, None, None, None

    # Initialize variables
    sum_elements = 0
    max_element = arr[0]
    min_element = arr[0]

    # Iterate over the array
    for i in range(n):
        # Update the sum of elements
        sum_elements += arr[i]
        
        # Update the maximum element
        if arr[i] > max_element:
            max_element = arr[i]
        
        # Update the minimum element
        if arr[i] < min_element:
            min_element = arr[i]

    # Calculate the average
    average = sum_elements / n

    return sum_elements, average, max_element, min_element