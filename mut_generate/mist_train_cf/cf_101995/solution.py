"""
QUESTION:
Write a function `find_index(lst, c)` that finds the index of the first occurrence of the element `c` in the list `lst`. The function should return the index of `c` if found, and a message or value indicating that `c` was not found otherwise. The solution must have a time complexity of O(n) and a space complexity of O(1), and must not use built-in functions or methods that directly solve the problem.
"""

def find_index(lst, c):
    index = -1
    for i in range(len(lst)):
        if lst[i] == c:
            index = i
            break
    if index == -1:
        return "Element not found"
    else:
        return index