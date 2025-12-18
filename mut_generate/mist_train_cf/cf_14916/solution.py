"""
QUESTION:
Define a function `print_list_elements(lst, counter, limit)` to recursively print the elements of a list `lst` starting from index `counter`, and stop after `limit` number of elements have been printed. Assume the initial value of `counter` is 0.
"""

def entance(lst, counter, limit):
    if counter == limit:
        return
    if counter < len(lst):
        print(lst[counter])
        entance(lst, counter+1, limit)