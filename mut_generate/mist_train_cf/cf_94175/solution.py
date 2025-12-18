"""
QUESTION:
Create a function called `reverse_copy` that takes an input list and returns a new list containing the same elements in reverse order. The function should not use any built-in list methods or functions, such as `reversed`, `reverse`, `extend`, or `list slicing`.
"""

def reverse_copy(original_list):
    reversed_list = []
    for i in range(len(original_list)-1, -1, -1):
        reversed_list.append(original_list[i])
    return reversed_list