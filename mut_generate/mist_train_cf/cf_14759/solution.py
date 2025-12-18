"""
QUESTION:
Write a function `generate_permutations` that takes a string as input and returns a list of all possible permutations of the string. The function should have a time complexity of O(n!), where n is the length of the string. The function should not include any duplicate permutations in the output list.
"""

def generate_permutations(string):
    if len(string) <= 1:
        return [string]
    
    permutations = []
    for i, char in enumerate(string):
        remaining = string[:i] + string[i+1:]
        for perm in generate_permutations(remaining):
            permutations.append(char + perm)
            
    return permutations