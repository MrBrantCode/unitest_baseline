"""
QUESTION:
Design a function `decompress_3d_array` that takes a three-dimensional array of floating point numbers as input and returns a new three-dimensional array where each floating point number is rounded to 5 decimal places.
"""

def decompress_3d_array(array):
    decompressed = []
    for i in array:
        temp_array_i = []
        for j in i:
            temp_array_j = []
            for k in j:
                temp_array_j.append(round(k, 5))
            temp_array_i.append(temp_array_j)
        decompressed.append(temp_array_i) 
    return decompressed