"""
QUESTION:
Implement a function `permutations(arr)` to generate all permutations of the given list of letters without using any built-in library functions or external modules. The function should handle lists with duplicate elements, return the permutations in lexicographically sorted order, and have a time complexity of O(n * n!). The function should not use any extra space except for the space required to hold the input and the output, and should avoid duplicate permutations.
"""

def generate_permutations(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]

    result = []
    used = set()

    for i in range(len(arr)):
        m = arr[i]
        
        rem_list = arr[:i] + arr[i+1:]
        
        if m in used:
            continue
        
        used.add(m)
        
        for p in generate_permutations(rem_list):
            result.append([m] + p)
            
    return sorted(result)