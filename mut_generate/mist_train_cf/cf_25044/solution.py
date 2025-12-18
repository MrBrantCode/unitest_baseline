"""
QUESTION:
Write a function called `switch_list` that takes a list of elements as input and returns a new list where the positions of the odd-indexed elements and the even-indexed elements are swapped. The function should modify the original list by swapping adjacent elements if their indices are of different parity (i.e., one is odd and the other is even). Note that if the list has an odd length, the last element will remain in its original position.
"""

def switch_list(mylist):
    for i in range(0, len(mylist) - 1, 2):
        mylist[i], mylist[i + 1] = mylist[i + 1], mylist[i]
    return mylist