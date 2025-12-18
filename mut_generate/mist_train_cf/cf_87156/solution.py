"""
QUESTION:
Write a function named `delete_element` that takes a 2D list `arr` and an index `index` as input. The function should delete the element at the given index in the 2D list and shift the elements in the same row and column to fill the gap. The index is a tuple of two integers representing the row and column indices. The function should return the modified 2D list. The input 2D list is not empty and the given index is within the bounds of the list. The function should handle the case where the 2D list is empty and the index is out of bounds by returning the original 2D list.
"""

def delete_element(arr, index):
    # Check if the array is empty
    if not arr:
        return arr

    # Get the number of rows and columns in the array
    num_rows = len(arr)
    num_cols = len(arr[0])

    # Check if the index is within the bounds of the array
    if index[0] < 0 or index[0] >= num_rows or index[1] < 0 or index[1] >= num_cols:
        return arr

    # Delete the element at the given index
    del arr[index[0]][index[1]]

    # Shift the elements in the same row to fill the gap
    for row in arr:
        if len(row) > num_cols:
            row.pop()

    # Shift the elements in the same column to fill the gap
    for i in range(num_rows):
        if len(arr[i]) > index[1]:
            del arr[i][index[1]]

    return arr