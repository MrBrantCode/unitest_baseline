"""
QUESTION:
Write a function named `sum_array` that calculates the sum of all elements in a three-dimensional array. The input will be a 3D array, and the function should return the total sum of all individual elements in the array.
"""

def sum_array(data):
    total = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            for k in range(len(data[i][j])):
                total += data[i][j][k]
    return total