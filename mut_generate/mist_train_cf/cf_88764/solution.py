"""
QUESTION:
Write a function named find_second_largest that takes an array of numbers as input and returns the second largest number in the array. The function must have a time complexity of O(n) and a space complexity of O(1), and it cannot use any built-in sorting or max functions. If the array has less than two elements, the function should return None.
"""

def find_second_largest(arr):
    if len(arr) < 2:
        return None
    
    largest = arr[0]
    second_largest = float('-inf')
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    
    return second_largest