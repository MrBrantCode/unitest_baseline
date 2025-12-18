"""
QUESTION:
Write a function named `permutations` that generates all possible permutations of the characters in a given string. The function should return a list of all unique permutations. The input string may be empty.
"""

def permutations(string):
    """
    Function to generate all possible permutations of a given string
    """
    if len(string) == 0:
        return ['']
    prev_list = permutations(string[1:len(string)])
    next_list = []
    for i in range(0,len(prev_list)):
        for j in range(0,len(string)):
            new_string = prev_list[i][0:j]+string[0]+prev_list[i][j:len(prev_list[i])]
            if new_string not in next_list:
                next_list.append(new_string)
    return next_list