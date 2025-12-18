"""
QUESTION:
Create a function `permutations` that generates all possible permutations of a given string. The function should accept strings of up to 10 characters and return a list of all permutations. If the input string exceeds 10 characters, the function should return an error message.
"""

def permutations(string):
    if len(string) > 10:
        return "Error: String length must be up to 10 characters."
    
    # Base case: if the string has only one character, return it as a single permutation
    if len(string) == 1:
        return [string]
    
    # Recursive case: for each character in the string, generate permutations with that character fixed
    result = []
    for i in range(len(string)):
        fixed_char = string[i]
        remaining_chars = string[:i] + string[i+1:]
        sub_permutations = permutations(remaining_chars)
        
        # Append each sub-permutation with the fixed character to the result
        for sub_permutation in sub_permutations:
            result.append(fixed_char + sub_permutation)
    
    return result