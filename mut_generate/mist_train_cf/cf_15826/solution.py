"""
QUESTION:
Write a function called `sum_of_odd_elements` that takes a 2D list `matrix` as input, where `matrix` can contain both positive and negative integers. The function must compute and return the sum of all odd elements in the `matrix` without using any extra space.
"""

def sum_of_odd_elements(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] % 2 != 0:
                sum += matrix[i][j]
    return sum