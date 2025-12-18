"""
QUESTION:
Create a function `print_third_highest(lst)` that takes a list of integers as input and prints the third highest unique value. If the list contains less than three unique values, print "The list doesn't have a third highest value." The function should consider duplicate values and handle them correctly.
"""

def print_third_highest(lst):
    unique_lst = list(set(lst))

    if len(unique_lst) < 3:
        print("The list doesn't have a third highest value.")
        return

    unique_lst.sort(reverse=True)
    print(unique_lst[2])