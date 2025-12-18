"""
QUESTION:
Write a function `find_equilibrium_indexes(arr)` that finds all the equilibrium indexes of the given array. An index of an array is called an equilibrium index if the sum of elements at lower indexes (excluding the element at the index itself) is equal to the sum of elements at higher indexes (excluding the element at the index itself). The function should return a list of all the equilibrium indexes found in the array. The function should have a time complexity of O(n) and space complexity of O(1), where n is the number of elements in the array.
"""

def find_equilibrium_indexes(arr):
    equilibrium_indexes = []
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        total_sum -= arr[i]
        
        if left_sum == total_sum:
            equilibrium_indexes.append(i)
            
        left_sum += arr[i]
        
    return equilibrium_indexes