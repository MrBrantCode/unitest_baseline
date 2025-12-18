"""
QUESTION:
Create a function named `reverse_and_remove_duplicates` that takes a list as input, reverses its order, removes any duplicates, and returns the modified list. The function must use constant space complexity and achieve a time complexity of O(n).
"""

def reverse_and_remove_duplicates(lst):
    lst.reverse()

    unique_set = set()

    i = len(lst) - 1
    while i >= 0:
        if lst[i] not in unique_set:
            unique_set.add(lst[i])
            i -= 1
        else:
            lst.pop(i)
            i -= 1

    return lst