"""
QUESTION:
Write a function named `generate_parentheses` that takes an integer `n` as input and returns all possible combinations of balanced parentheses with `n` pairs. The function should use recursion to generate the combinations. The output should be a list of strings, where each string represents a valid combination of balanced parentheses.
"""

def generate_parentheses(n):
    result = []
    
    # Recursive helper function
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    
    backtrack('', 0, 0)
    return result