"""
QUESTION:
Write a Python function `median` that calculates the median of a given list of numbers. The function should first check if the list is empty and return a message if it is. Then, it should sort the list in ascending order without modifying the original list. Finally, it should return the median of the sorted list, which is the middle number if the list has an odd length and the average of the two middle numbers if the list has an even length.
"""

def median(l):
    # checking if list is empty
    if not l:
        return "List is empty"

    # cloning the list to avoid mutation
    copy_list = l.copy()

    # insertion sort
    for i in range(1, len(copy_list)):
        value_to_sort = copy_list[i]
        while copy_list[i - 1] > value_to_sort and i > 0:
            copy_list[i], copy_list[i - 1] = copy_list[i - 1], copy_list[i]
            i -= 1

    if len(copy_list) % 2 != 0:
        return float(copy_list[int((len(copy_list) - 1) / 2)])
    else:
        # average of the middle numbers when list count is even
        return float((copy_list[int((len(copy_list) / 2) - 1)] + copy_list[int(len(copy_list) / 2)]) / 2)