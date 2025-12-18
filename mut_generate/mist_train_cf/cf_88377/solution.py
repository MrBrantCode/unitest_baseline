"""
QUESTION:
Define a function `search_element(arr, element, start_row, start_col, end_row, end_col)` that searches for a specific element in a two-dimensional array `arr` within a specific subregion defined by `start_row`, `start_col`, `end_row`, and `end_col`. The function should return the indices of all occurrences of the element as a list of tuples. If the element is not found, the function should return an empty list. The function must be implemented using a recursive approach and should only perform the search on the specified subregion of the two-dimensional array.
"""

def search_element(arr, element, start_row, start_col, end_row, end_col):
    # Base case: If the subregion is empty or out of bounds, return an empty list
    if start_row > end_row or start_col > end_col:
        return []

    # Check if the current element is equal to the target element
    if arr[start_row][start_col] == element:
        # If yes, add the current indices to the result list
        result = [(start_row, start_col)]
    else:
        result = []

    # Recursive case: Search in the next column of the current row
    if start_col < end_col:
        result += search_element(arr, element, start_row, start_col + 1, end_row, end_col)

    # Recursive case: Search in the next row of the current column
    if start_row < end_row:
        result += search_element(arr, element, start_row + 1, start_col, end_row, end_col)

    return result