"""
QUESTION:
Create a function named `calculate_sum` that takes an array of positive integers as a parameter and returns the total sum of all valid items (where a valid item is an item that is larger than the previous item) along with the index of the largest valid item. The function must have a time complexity of O(n), where n is the number of elements in the array.
"""

def calculate_sum(arr):
    total_sum = 0
    max_index = -1
    
    for i in range(len(arr)):
        if i > 0 and arr[i] > arr[i-1]:
            total_sum += arr[i]
            if arr[i] > arr[max_index] or max_index == -1:
                max_index = i
    
    return total_sum, max_index