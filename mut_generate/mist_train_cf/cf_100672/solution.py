"""
QUESTION:
Create a function called `custom_rotate` that takes in three parameters: an array of strings `arr`, a subset of elements to be rotated `subset`, and a string operation `operation` to be performed on the rotated elements. The function should rotate the elements in `subset` along a different axis than -1, apply the specified `operation` to the rotated elements, and incorporate them back into the original array `arr`. The function should use only built-in Python functions and not utilize slicing syntax.
"""

def custom_rotate(arr, subset, operation):
    # create a new list to store the rotated subset
    rotated_subset = []
    # perform the specified string operation on each element in the subset
    for elem in subset:
        rotated_subset.append(operation(elem))
    # remove the subset from the original array and save it in a separate list
    subset_indices = []
    for i in range(len(arr)):
        if arr[i] in subset:
            subset_indices.append(i)
    rotated_subset_indices = [(subset_indices[i] - subset_indices[0] + 1) % len(subset) for i in range(len(subset_indices))]
    removed_subset = []
    for i in range(len(subset_indices)):
        removed_subset.append(arr.pop(subset_indices[i] - i))
    # insert the rotated subset back into the array
    for i in range(len(rotated_subset_indices)):
        arr.insert(subset_indices[i], rotated_subset[rotated_subset_indices[i]])
    return arr