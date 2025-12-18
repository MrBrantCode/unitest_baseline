"""
QUESTION:
Create a function `split_list(n, mylist)` that takes an integer `n` and a list `mylist` as inputs, splits `mylist` into two parts such that the length of the first part is `n`, and returns these two parts. If `n` is out of the range of the list's length, print an error message instead.
"""

def split_list(n, mylist):
    if n < 0 or n > len(mylist):
        print("Your input is out of range of the list's length.")
        return
    part1 = mylist[0:n]
    part2 = mylist[n:]
    return part1, part2