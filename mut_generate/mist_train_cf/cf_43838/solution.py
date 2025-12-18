"""
QUESTION:
Write a function `eradicate_three` that takes a list of integers as input and returns a new list where all instances of the number 3 are removed, unless three consecutive numbers sum up to 3, in which case only the first of these three numbers is removed. The function should modify the list in-place and return the modified list.
"""

def eradicate_three(mylist):
    i = 0
    while i < len(mylist):
        if i < len(mylist) - 2 and sum(mylist[i:i+3]) == 3:
            del mylist[i]
        elif mylist[i] == 3:
            del mylist[i]
        else:
            i += 1
    return mylist