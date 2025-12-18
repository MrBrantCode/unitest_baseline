"""
QUESTION:
Write a function `permute(s)` that generates all unique permutations of the given string `s`. The function should be able to handle strings with duplicate characters and should not include duplicate permutations in the output. The time complexity of the function should be O(n * 2^n) and the space complexity should be O(n * 2^n).
"""

def permute(s):
    # Base case: if string is empty, return empty permutation
    if len(s) == 0:
        return ['']
    
    # Sort the string to handle duplicates
    s = ''.join(sorted(s))
    
    # Initialize a list to store all permutations
    permutations = []
    
    # Iterate through each character in the string
    for i in range(len(s)):
        # Exclude duplicates by skipping if the character is the same as the previous one
        if i > 0 and s[i] == s[i-1]:
            continue
        
        # Generate permutations for the remaining characters
        remaining = s[:i] + s[i+1:]
        for p in permute(remaining):
            # Add the current character to each permutation of the remaining characters
            permutations.append(s[i] + p)
    
    return permutations