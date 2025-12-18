"""
QUESTION:
Write a function `generateParenthesis(N)` to generate all possible combinations of balanced parentheses with `N` pairs. The function should return a list of strings, each representing a combination of balanced parentheses. The function must only use valid parentheses combinations where every open parenthesis can be matched with a corresponding close parenthesis, and vice versa.
"""

def generateParenthesis(N): 
    result = [] 
  
    def generate(left, right, string): 
        if (left == 0 and right == 0): 
            result.append(string) 
            return
  
        if left > 0: 
            generate(left - 1, right, string + "(") 
  
        if left < right: 
            generate(left, right - 1, string + ")") 
  
    if N > 0: 
        generate(N, N, "") 
    return result