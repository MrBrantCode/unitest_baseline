"""
QUESTION:
Write a function `find_vect` that takes a 3D array `lst3d` and two integers `x` and `y` as input, and returns a list of triplets representing the coordinates (depth, row, index) of all occurrences of the sub-vector `[x, y]` in the 3D array. The returned list should be sorted in ascending order by depth, then by row, and finally by index.
"""

def find_vect(lst3d, x, y):
    indices = []
    for i in range(len(lst3d)):
        for j in range(len(lst3d[i])):
            for k in range(len(lst3d[i][j]) - 1):
                if lst3d[i][j][k] == x and lst3d[i][j][k + 1] == y:
                    indices.append((i, j, k))
                    
    indices.sort()
    return indices