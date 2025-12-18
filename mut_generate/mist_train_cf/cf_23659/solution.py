"""
QUESTION:
Write a function called `permutation` that generates all unique permutations for a given string. The function should take a string as input and return a list of all possible permutations as strings. The order of the permutations does not matter.
"""

def permutation(s):
    if len(s) == 0: 
        return [] 
    if len(s) == 1: 
        return [s]  
    result = []  
    for i in range(len(s)): 
       m = s[i]  
       remLst = s[:i] + s[i+1:]  
       for p in permutation(remLst): 
           result.append(m + p) 
    return result 