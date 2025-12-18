"""
QUESTION:
Create a function named `generate_array` that creates an array of numbers from 1 to n in descending order without using any loops or built-in functions. Implement another function named `binary_search` that takes the generated array and a target number as input, and returns the index of the target number in the array using the binary search algorithm. The binary search function should return -1 if the target number is not found in the array.
"""

def generate_array(n):
    if n == 1:
        return [1]
    else:
        return [n] + generate_array(n-1)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1