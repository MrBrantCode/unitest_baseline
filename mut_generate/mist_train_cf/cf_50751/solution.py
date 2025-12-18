"""
QUESTION:
Write a recursive function `find_smallest_num` that takes a list of integers as input and returns the smallest number in the list. The function should be able to handle a list of any length, but it must use recursion to find the smallest number. The list will not be empty and will only contain integers.
"""

def find_smallest_num(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        smallest_other = find_smallest_num(num_list[1:])
        return num_list[0] if num_list[0] < smallest_other else smallest_other