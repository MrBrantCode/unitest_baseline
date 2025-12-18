"""
QUESTION:
Design a function named `find_occurrences` that takes a list of strings (`lst`) and a target string (`strr`) as input and returns a list containing the indices of the first and last occurrences of `strr` in `lst`. The function should return [-1, -1] if `strr` does not exist in `lst`. The indices should be 0-based, meaning the first element of `lst` has an index of 0.
"""

def find_occurrences(lst, strr):
    first_occurrence = -1
    last_occurrence = -1

    for i in range(len(lst)):
        if lst[i] == strr:
            if first_occurrence == -1:
                first_occurrence = i
            last_occurrence = i

    return [first_occurrence, last_occurrence]