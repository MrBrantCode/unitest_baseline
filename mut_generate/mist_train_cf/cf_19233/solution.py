"""
QUESTION:
Create a function `generate_permutations` that generates n! permutations of a given array. The function should not use the itertools library or any built-in functions that directly solve this problem. The input parameters are an array `arr` and an integer `n`, and the function should return a list of all permutations, where each permutation is a list of elements from the input array.
"""

def generate_permutations(arr, n):
    permutations = []
    permute(arr, [], permutations, n)
    return permutations

def permute(arr, temp, permutations, n):
    # If the temporary array is of length n, a permutation is complete
    if len(temp) == n:
        permutations.append(temp[:])  # make a copy of the current permutation
        return
    
    for i in range(len(arr)):
        # Choose the i-th element as the next element in the permutation
        temp.append(arr[i])
        
        # Remove the chosen element from the input array
        remaining = arr[:i] + arr[i+1:]
        
        # Generate permutations with the remaining elements
        permute(remaining, temp, permutations, n)
        
        # Backtrack by removing the last element from the temporary array
        temp.pop()