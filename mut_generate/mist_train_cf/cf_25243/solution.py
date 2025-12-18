"""
QUESTION:
Write a function named `generate_permutations` that generates an array of all possible permutations of N numbers. The function should take an integer `n` as input and return a list of lists, where each sublist is a unique permutation of the numbers from 1 to `n`. The function should handle the base cases where `n` is 0 or 1 and return the correct permutations for these cases.
"""

def generate_permutations(n): 
    if n == 0: 
        return [] 
    
    if n == 1: 
        return [[1]] 
  
    permutations = [] 
    for i in range(n): 
        permutations_n_1 = generate_permutations(n - 1) 
  
        for perm in permutations_n_1: 
            for j in range(n): 
                r = perm.copy() 
                r.insert(j, n) 
                permutations.append(r) 
  
    return permutations