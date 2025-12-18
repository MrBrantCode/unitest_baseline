"""
QUESTION:
Find the closest pair of elements in an array with respect to a given target number. 

Create a function named `closest_pair` that takes two parameters: an array of integers (`arr`) and a target number (`target`). The function should return the indices of the pair of elements in the array whose sum is closest to the target number. The array contains distinct integers and the pair should be unique, i.e., the pair should not contain the same index twice.
"""

def closest_pair(arr, target): 
    min_difference = float('inf')
    min_pair = (-1, -1)
      
    for i in range(len(arr)): 
        for j in range(i + 1, len(arr)): 
            diff = abs(arr[i] + arr[j] - target) 
            if diff < min_difference: 
                min_difference = diff 
                min_pair = (i, j) 
      
    return min_pair