"""
QUESTION:
Write a function `permutations` that generates all possible permutations of a given input string. The function should return a list of all permutations, where each permutation is a string. For example, given the input string "abc", the function should return a list containing all possible orderings of "a", "b", and "c". The input string may be empty or contain duplicate characters.
"""

def permutations(string): 
    if len(string) == 0: 
        return [] 
  
    if len(string) == 1: 
        return [string] 
  
    result = [] 
    for i in range(len(string)): 
       char = string[i] 
       rem_string = string[:i] + string[i+1:] 
       for p in permutations(rem_string): 
           result.append(char + p) 
    return result