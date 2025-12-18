"""
QUESTION:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



For example, given n = 3, a solution set is:


[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

def generate_parenthesis(n):
    def generate(left, right, result, string):
        if left == 0 and right == 0:
            result.append(string)
            return
        if left > 0:
            generate(left - 1, right, result, string + '(')
        if left < right:
            generate(left, right - 1, result, string + ')')
    
    if n == 0:
        return []
    
    result = []
    generate(n, n, result, '')
    return result