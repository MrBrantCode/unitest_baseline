"""
QUESTION:
Write a function `permutation` that takes a string `s` as input and returns all its unique permutations as a list. The function should be able to handle strings of up to length 50 and return an error message if the input string is longer than that. The function should achieve a time complexity of O(n * n!) and a space complexity of O(n!), where n is the length of the input string.
"""

def permutation(s):
    if len(s) > 50:
        return "Input string too long"
    
    unique_permutations = set()
    
    def backtrack(s, current_permutation):
        if not s:
            unique_permutations.add(current_permutation)
        else:
            for i in range(len(s)):
                backtrack(s[:i] + s[i+1:], current_permutation + s[i])
    
    backtrack(s, "")
    
    return list(unique_permutations)