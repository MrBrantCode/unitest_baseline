"""
QUESTION:
Create a function `create_3D_array` that takes a list of 27 integers as input and returns a 3x3x3 3D array. The input list should be reshaped such that the first 9 elements form the first 2D array, the next 9 elements form the second 2D array, and the last 9 elements form the third 2D array. Within each 2D array, the elements should be divided into three 3-element arrays. The function should return the resulting 3D array.
"""

def create_3D_array(input_list):
    array_3D = []
    for i in range(0, len(input_list), 9):
        array_2D = []
        for j in range(i, i+9, 3):
            array_2D.append(input_list[j:j+3])
        array_3D.append(array_2D)
    return array_3D