"""
QUESTION:
Write a function called `permuteString(s)` that returns all possible permutations of a given string `s` using a recursive approach. The function should handle duplicate characters by not including duplicate permutations in the output and correctly handle an empty string input. The time complexity of the function should be O(n!), where n is the length of the string.
"""

def permuteString(s):
    permutations = []
    
    if len(s) == 0:
        return permutations
    
    def generatePermutations(curr, remaining, permutations):
        if len(remaining) == 0:
            permutations.append(curr)
            return
        
        for i in range(len(remaining)):
            if i > 0 and remaining[i] == remaining[i-1]:
                continue
            
            new_curr = curr + remaining[i]
            new_remaining = remaining[:i] + remaining[i+1:]
            
            generatePermutations(new_curr, new_remaining, permutations)
    
    s = ''.join(sorted(s))
    generatePermutations('', s, permutations)
    
    return permutations