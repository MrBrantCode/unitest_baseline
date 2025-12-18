"""
QUESTION:
Create a function `find_position` that takes in two arguments, a sorted array and a number, and returns the position of the number in the array. The function should have a time complexity of O(log n) or better, where n is the length of the array, and use a recursive binary search algorithm.
"""

def find_position(arr, num):
    def binary_search(low, high):
        if low > high:
            return -1
        
        mid = (low + high) // 2
        
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            return binary_search(low, mid - 1)
        else:
            return binary_search(mid + 1, high)
    
    return binary_search(0, len(arr) - 1)