"""
QUESTION:
Write a function `find_min` that takes a 2D array as input and returns the minimum element. The solution should not use built-in Python functions like `min()` and sorting algorithms.
"""

def find_min(my_2d_array):
    minn = my_2d_array[0][0] 
    for i in range(len(my_2d_array)):
        for j in range(len(my_2d_array[i])):
            if minn > my_2d_array[i][j]:
                minn = my_2d_array[i][j] 
    return minn 