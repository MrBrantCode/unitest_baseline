"""
QUESTION:
Create a function called `permutation` that generates all permutations of a given input string. The function should return a list of lists, where each sublist is a permutation of the input string. The function should work for any input string, but it is only required to work for strings containing unique characters.
"""

def permutation(s):
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [[s]]
    result = [] 
    for i in range(len(s)):
       char = s[i] 
       remLst = permutation(s[:i] + s[i+1:])
       for p in remLst:
           result.append([char] + p)
    return result