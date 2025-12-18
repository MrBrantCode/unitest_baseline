"""
QUESTION:
Write a function named `move_zeroes_to_end` that takes a list as an argument. The function should move all zeroes in the list to the end while maintaining the relative order of non-zero elements. If the list contains nested lists, the function should recursively move all zeroes in the nested lists to the end of their respective lists. Do not use built-in Python functions or libraries to directly solve this problem.
"""

def move_zeroes_to_end(lst):
    # create superfunction to use recursively 
    def move_zeroes(lst1):
        count = lst1.count(0)
        res = [i for i in lst1 if i != 0]
        res.extend([0]*count)
        return res
    # check if list is nested and if so apply function recursively 
    for i, sublist in enumerate(lst):
        if type(sublist) is list:
            lst[i] = move_zeroes_to_end(sublist)
        else:
            lst = move_zeroes(lst)
    return lst