"""
QUESTION:
Write a function `permuteString(s)` that returns all possible unique permutations of a given string `s`, where `s` may contain duplicate characters. The function should use a recursive approach, handle the input of an empty string correctly, and have a time complexity of O(n!), where n is the length of the string.
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