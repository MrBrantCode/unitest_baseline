"""
QUESTION:
Create a function named `eradicate_threes` that takes a list `mylist` as input and returns the modified list with all instances of the number 3 removed, including those in nested lists, while maintaining the original nested structure. The function should handle consecutive instances of 3 correctly and preserve the data type of nested lists.
"""

def eradicate_threes(mylist):
    i = 0
    while i < len(mylist):
        if mylist[i] == 3: 
            mylist.pop(i)
        elif isinstance(mylist[i], list):
            mylist[i] = eradicate_threes(mylist[i])
            i += 1
        else: 
            i += 1
    return mylist