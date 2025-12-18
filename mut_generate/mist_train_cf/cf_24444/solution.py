"""
QUESTION:
Write a function called `permute` that generates all unique permutations of a given string. The function should take a string as input and return a list of all possible permutations. The input string can be of any length, but it is assumed to be non-empty. The function should not contain any duplicate permutations in the output.
"""

def permute(string):
    if len(string) == 1:
        return [string] 

    prevList = permute(string[1:]) 

    nextList = [] 
    for i in range(len(prevList)): 
        for j in range(len(string)): 
            newString = prevList[i][:j] + string[0:1] + prevList[i][j:] 
            if newString not in nextList: 
                nextList.append(newString) 
    return nextList