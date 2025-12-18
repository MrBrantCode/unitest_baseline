"""
QUESTION:
Write a function `find_triplets` that takes an array of integers and a target value as input, and returns a list of all triplets of elements in the array whose sum is equal to the target value. The function should have a time complexity of O(n^3) and should not use any built-in sorting functions.
"""

def find_triplets(array, target):
    triplets = []
    n = len(array)
    
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if array[i] + array[j] + array[k] == target:
                    triplets.append((array[i], array[j], array[k]))
    
    return triplets