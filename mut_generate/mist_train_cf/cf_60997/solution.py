"""
QUESTION:
Write a function called `find_indices` that takes a list of strings and a distinct string as input. The function should return the indices of two strings from the list whose total character count is equivalent to the character count of the given distinct string. It is guaranteed that each input will have a unique solution, and the same string cannot be used twice.
"""

def find_indices(string_list, target):
    target_len = len(target)
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if len(string_list[i]) + len(string_list[j]) == target_len:
                return [i, j]