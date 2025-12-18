"""
QUESTION:
Write a function `median` that takes an unsorted list `l` of numbers as input and returns the median of the list. The function should handle lists with negative numbers, floating point numbers, duplicate numbers, large numbers, and lists of even and odd lengths. The function should not use any built-in sorting functions or list sorting methods. If the input list is empty, the function should return a message indicating that the list is empty.
"""

def find_median(l):
    
    #checking if list is empty
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