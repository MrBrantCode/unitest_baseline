"""
QUESTION:
Create a function named `create_2d_array` that takes two parameters: `rows` and `cols`, representing the dimensions of the 2D array. The function should return a 2D array of size `rows` x `cols` where all elements are unique and in ascending order. The time complexity of the function should be O(n), where n is the total number of elements in the array (`rows` * `cols`).
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