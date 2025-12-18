"""
QUESTION:
Create a Python function called `sort_3d_array` that sorts a 3D array based on the numerical value of the third element in each subordinate array. The function should handle cases where a subordinate array has fewer than three elements, and it should sort the array in ascending order by default.
"""

def sort_3d_array(arr):
    """Sorts a 3d array based on the third element in each sub-array."""

    # Error handling for arrays that don't have a third element
    try:
        return sorted(arr, key=lambda x: x[2])
    except IndexError:
        print("One or more elements in the array do not have a third element.")