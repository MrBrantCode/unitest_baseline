"""
QUESTION:
Write a function `generate_permutations(items)` that generates all permutations of a given list of items, excluding any permutations that contain consecutive repeating elements. The function should return a list of lists, where each sublist is a permutation of the input list.
"""

def generate_permutations(items):
    def backtrack(permutation, remaining, permutations):
        if len(remaining) == 0:
            permutations.append(permutation)
            return
        
        for i in range(len(remaining)):
            if len(permutation) > 0 and permutation[-1] == remaining[i]:
                continue
            
            backtrack(
                permutation + [remaining[i]],
                remaining[:i] + remaining[i+1:],
                permutations
            )
    
    permutations = []
    backtrack([], items, permutations)
    return permutations