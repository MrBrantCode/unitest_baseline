"""
QUESTION:
Define a function `closestPair(array, target)` that finds the closest pair of elements in a given array with respect to a given target number. The array contains at most 10^6 elements and the target number is within the range of -10^9 to 10^9. The function should return the pair of elements that have the smallest absolute difference with the target number. If there are multiple pairs with the same smallest absolute difference, return any one of them. The function should not use any built-in sorting or searching functions and have a time complexity of O(nlogn), where n is the size of the array.
"""

def closestPair(array, target):
    array = mergeSort(array)  # Sort the array using merge sort
    minDiff = float('inf')    # Initialize minimum difference to positive infinity
    closestPair = []          # Initialize closest pair as an empty list
    
    for i in range(len(array) - 1):
        diff = abs(array[i] - target)  # Calculate difference
        
        if diff < minDiff:
            minDiff = diff
            closestPair = [array[i], array[i+1]]
        elif diff == minDiff:
            if array[i] + array[i+1] < closestPair[0] + closestPair[1]:
                closestPair = [array[i], array[i+1]]
    
    return closestPair

def mergeSort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    
    left = mergeSort(left)    # Recursive call to sort the left half
    right = mergeSort(right)  # Recursive call to sort the right half
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])   # Add remaining elements from left list
    result.extend(right[j:])  # Add remaining elements from right list
    
    return result