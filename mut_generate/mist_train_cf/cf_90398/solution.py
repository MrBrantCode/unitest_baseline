"""
QUESTION:
Implement a function called `mergeSortDescending` that sorts an array in descending order without using any built-in sorting functions or methods. The function must have a time complexity of O(n log n) and cannot use any additional data structures or variables beyond what is necessary for the implementation. It should also limit the use of nested loops to a maximum of three.
"""

def mergeSortDescending(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = mergeSortDescending(left)
    right = mergeSortDescending(right)
    
    result = []
    leftIndex = rightIndex = 0
    
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] >= right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1
    
    while leftIndex < len(left):
        result.append(left[leftIndex])
        leftIndex += 1
    
    while rightIndex < len(right):
        result.append(right[rightIndex])
        rightIndex += 1
    
    return result