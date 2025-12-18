"""
QUESTION:
Write a function count(x, y, z, n) that calculates the length of the minimal sequence describing a 2^n x 2^n x 2^n 3D image D_n, where the voxel with coordinates x = 0, y = 0, z = 0 corresponds to the bottom front left voxel, and a voxel is black if it is contained within a certain euclidean distance from the center of the cube, otherwise it is white. The function should return the length of the minimal sequence.
"""

def count(x, y, z, n):
    if n == 0:
        return 1
    if (x-2**(n-1))**2 + (y-2**(n-1))**2 + (z-2**(n-1))**2 <= 2**(3*n-3):
        if (x+1)**2 + y**2 + z**2 <= 2**(3*n-3):
            return 2
        else:
            return 1 + 8*count(x,y,z,n-1)
    elif (x+2**(n-1))**2 + (y+2**(n-1))**2 + (z+2**(n-1))**2 > 2**(3*n-3):
        return 2
    else:
        return 1 + 8*count(x,y,z,n-1)