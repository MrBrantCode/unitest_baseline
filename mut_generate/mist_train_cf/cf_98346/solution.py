"""
QUESTION:
Implement a function named `custom_rotate` that takes three parameters: a list of strings `arr`, a list of strings `subset`, and a function `operation`. The function should perform the following operations:

- Rotate the elements in `subset` along a different axis than -1.
- Perform the specified string operation on the shifted elements.
- Incorporate the rotated elements back into the original list `arr`.

Restrictions:

- Use only built-in Python functions.
- Do not use slicing syntax (i.e., [:], [::], etc.).
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