"""
QUESTION:
Write a function named `permutations` that takes a string as input and returns all possible permutations of the string. The function should handle strings of up to 10 characters and return an error message if the input string is longer than that.
"""

def permutations(string):
    if len(string) > 10:
        return "Error: String length must be up to 10 characters."
    
    if len(string) == 1:
        return [string]
    
    result = []
    for i in range(len(string)):
        fixed_char = string[i]
        remaining_chars = string[:i] + string[i+1:]
        sub_permutations = permutations(remaining_chars)
        
        for sub_permutation in sub_permutations:
            result.append(fixed_char + sub_permutation)
    
    return result