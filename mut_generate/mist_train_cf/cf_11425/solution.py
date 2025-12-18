"""
QUESTION:
Write a function `generate_permutations` that generates all permutations of a given string. The function should take a string as input and return a list of all possible permutations. The length of the input string can be up to 10 characters.
"""

def generate_permutations(string):
    if len(string) == 1:
        return [string]
    
    permutations = []
    
    for i in range(len(string)):
        remaining_chars = string[:i] + string[i+1:]
        
        for permutation in generate_permutations(remaining_chars):
            permutations.append(string[i] + permutation)
    
    return permutations