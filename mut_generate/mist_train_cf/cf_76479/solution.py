"""
QUESTION:
Write a function `max_num(lst, i=-1, largest=float('-inf'))` that determines the largest number in a list using recursion. The function should take a list of numbers and two optional parameters, `i` and `largest`, where `i` is the current index and `largest` is the largest number found so far. The function should return the largest number in the list.
"""

def max_num(lst, i=-1, largest=float('-inf')):
    if abs(i) == len(lst) + 1: 
        return largest
    else: 
        if lst[i] > largest: 
            largest = lst[i]
        return max_num(lst, i - 1, largest)