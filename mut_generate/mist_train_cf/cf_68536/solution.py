"""
QUESTION:
Implement a function `find_element` that takes a 3D array `array3D` and a target value `target` as input and returns the location of the target value within the 3D array in terms of its indices (z, y, x). The 3D array is not guaranteed to be sorted.
"""

def find_element(array3D, target):
    for z in range(len(array3D)):
        for y in range(len(array3D[z])):
            for x in range(len(array3D[z][y])):
                if array3D[z][y][x] == target:
                    return (z, y, x)
    return None