"""
QUESTION:
Create a function named `extractTertiary` that takes a list `my_list` and an integer `n` as input. The function should return the third element of `my_list` if it has at least `n` elements. If `my_list` is a list of lists, return a list of third elements from each sublist. If `my_list` has less than `n` elements, return an error message "Error: List contains less than n elements".
"""

def extractTertiary(my_list, n):
    if len(my_list) < n:
        return "Error: List contains less than n elements"
    else:
        if isinstance(my_list[0], list):
            return [x[2] for x in my_list if len(x) >= 3]
        else:
            return my_list[2]