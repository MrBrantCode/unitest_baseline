"""
QUESTION:
Create a function `sort_tuples` that sorts a list of tuples in descending order of scores. If multiple tuples have the same score, they should be sorted in descending order of names. If multiple tuples have the same score and name, they should be sorted in descending order of their respective ID numbers. The input list will contain tuples of the format (name, score, ID number). The function should return the sorted list of tuples.
"""

def sort_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: (-x[1], -ord(x[0][0]), -x[2]))