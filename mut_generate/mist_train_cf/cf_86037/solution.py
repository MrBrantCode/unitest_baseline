"""
QUESTION:
Write a function called `switch_elements` that takes in a list and two indices, `pos1` and `pos2`, and swaps the elements at these positions in the list. The function should return the modified list if the indices are valid (i.e., within the range of the list), and `None` otherwise.
"""

def switch_elements(arr, pos1, pos2):
    # check if positions are valid
    if pos1 >= len(arr) or pos2 >= len(arr) or pos1 < 0 or pos2 < 0:
        return None
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr