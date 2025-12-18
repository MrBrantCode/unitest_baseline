"""
QUESTION:
Implement a function called `find_index` that takes a list and an element 'c' as input. The function should return the index of the first occurrence of 'c' in the list. If 'c' is not found in the list, the function should return "Element not found". The time complexity should be O(n) and the space complexity should be O(1), where n is the number of elements in the list. Do not use any built-in functions or methods that directly solve the problem.
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