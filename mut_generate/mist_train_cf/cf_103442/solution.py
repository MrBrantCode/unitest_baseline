"""
QUESTION:
Implement the function `switch_list(mylist)` that takes a list of positive integers `mylist` as input and returns a new list with the odd elements and even elements switched. The order of the elements should remain the same. The length of `mylist` will not exceed 10^5 and the function should have a time complexity of O(N), where N is the length of the input list.
"""

def switch_list(mylist):
    n = len(mylist)
    for i in range(0, n-1, 2):
        mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
    return mylist