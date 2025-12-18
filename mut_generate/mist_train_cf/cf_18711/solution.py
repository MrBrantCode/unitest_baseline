"""
QUESTION:
Create a function `remove_apple` that takes a list of fruits as input and returns a tuple containing a new list with all occurrences of 'apple' removed and a list of indices of the removed 'apple' elements. The function should not use the built-in `remove()` function. The input list may be empty and may contain duplicate elements, including 'apple' at different indices.
"""

def remove_apple(fruits):
    indices = []
    new_list = []
    
    for i in range(len(fruits)):
        if fruits[i] != 'apple':
            new_list.append(fruits[i])
        else:
            indices.append(i)
    
    return new_list, indices