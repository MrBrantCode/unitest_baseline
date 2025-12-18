"""
QUESTION:
Create a function named `find_element_indices` that takes a 5x5 2D array `arr`, and an element as input, and returns the index/indices of the element in the array. The function should return a list of tuples, where each tuple consists of two values: the row index and the column index. The function should be able to search for any type of element, including integers and strings. If the element is not present in the array, the function should return "Element not found in the array".
"""

def find_element_indices(arr, row_length, col_length, element):
    indices = []
    
    for i in range(row_length):
        for j in range(col_length):
            if arr[i][j] == element:
                indices.append((i, j))
                
    if not indices:
        return "Element not found in the array"
    
    return indices