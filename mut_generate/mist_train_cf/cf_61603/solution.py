"""
QUESTION:
Create a function `count_zeros` that takes a 3-dimensional array as input and returns the number of zero elements in the array. The function should use only basic loop structures and conditionals, without relying on any library's built-in functions for counting or array manipulation. The input array will be a 3D list of lists of lists, where each element is a number.
"""

def count_zeros(arr):
    """Function to traverse the 3D array and count the number of zero elements"""
    zero_count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(len(arr[i][j])):
                if arr[i][j][k] == 0:
                    zero_count += 1
    return zero_count