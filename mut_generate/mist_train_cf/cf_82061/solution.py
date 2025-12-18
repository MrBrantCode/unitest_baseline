"""
QUESTION:
Write a function named `find_sum` that takes a two-dimensional array `lst` and a target value `val` as input. The function should find any two integers in the nested arrays with odd indices in `lst` that add up to `val`, and return these two integers as a tuple. If no such pair is found, the function should return `None`.
"""

def find_sum(lst, val):
    for i in range(len(lst)):
        if i % 2 != 0: #check if index is odd
            for j in range(len(lst[i])):
                for k in range(j+1, len(lst[i])):
                    if lst[i][j] + lst[i][k] == val:
                        return (lst[i][j], lst[i][k])
    return None