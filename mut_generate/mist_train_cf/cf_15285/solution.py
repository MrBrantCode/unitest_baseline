"""
QUESTION:
Create a function `create_2d_array(rows, cols)` that generates a 2D array with the specified number of rows and columns, ensuring all elements are unique and in ascending order. The function should handle cases where `rows * cols` is less than or equal to 0. The time complexity of the function should be O(n), where n is the total number of elements in the array.
"""

def create_2d_array(rows, cols):
    if rows * cols <= 0:
        return []
    
    if rows == 1 and cols == 1:
        return [[1]]
    
    array = []
    num = 1
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(num)
            num += 1
        array.append(row)
    
    return array