"""
QUESTION:
Write a function `permutation(str)` that generates all possible permutations of characters in the input string `str` and returns them as a list of strings. The function should handle strings of any length, including empty strings, and should not contain duplicate permutations in the output.
"""

def entance(str):
    if len(str) == 0: 
        return [''] 
    prev_list = entance(str[1:len(str)]) 
    next_list = [] 
    for i in range(0,len(prev_list)): 
        for j in range(0,len(str)): 
            new_str = prev_list[i][0: j]+str[0]+prev_list[i][j: len(str)-1] 
            if new_str not in next_list: 
                next_list.append(new_str) 
    return next_list