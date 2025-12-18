"""
QUESTION:
Write a function `threeD_array_product` that calculates the product of elements along the two diagonals of a 3D cube array. The function should take a 3D array as input and return a tuple containing the product of the main diagonal (from the top-left-front to the bottom-right-back) and the product of the anti-diagonal (from the top-left-back to the bottom-right-front). The 3D array is a list of 3x3 matrices, where each element is an integer. The function should work for 3x3x3 arrays only.
"""

def threeD_array_product(arr):
    product1, product2 = 1, 1

    for i in range(len(arr)):
        product1 *= arr[i][i][i]
        product2 *= arr[i][i][len(arr) - 1 - i]

    return product1, product2