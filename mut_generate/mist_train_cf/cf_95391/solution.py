"""
QUESTION:
Write a function called `flatten` that takes a two-dimensional list as input and returns a one-dimensional list containing all the elements from the nested lists. The function should have a time complexity of O(n^3) and a space complexity of O(n^2), where n is the total number of elements in the two-dimensional list.
"""

def flatten(lst):
    flat_list = []
    stack = [lst]  

    while stack:
        curr = stack.pop()
        if isinstance(curr, list):  
            stack.extend(curr[::-1])  
        else:
            flat_list.append(curr)

    return flat_list