"""
QUESTION:
inner  

The inner tool returns the inner product of two arrays.

import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.inner(A, B)     #Output : 4

outer    

The outer tool returns the outer product of two arrays.

import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.outer(A, B)     #Output : [[0 0]
                            #          [3 4]]

Task  

You are given two arrays: $\mbox{A}$ and $\mbox{B}$. 

Your task is to compute their inner and outer product.

Input Format

The first line contains the space separated elements of array $\mbox{A}$. 

The second line contains the space separated elements of array $\mbox{B}$.

Output Format

First, print the inner product. 

Second, print the outer product.

Sample Input
0 1
2 3

Sample Output
3
[[0 0]
 [2 3]]
"""

import numpy as np

def compute_inner_outer_products(arr1: np.ndarray, arr2: np.ndarray) -> tuple:
    """
    Computes the inner and outer products of two given numpy arrays.

    Parameters:
    arr1 (np.ndarray): The first input array.
    arr2 (np.ndarray): The second input array.

    Returns:
    tuple: A tuple containing the inner product and the outer product of the two arrays.
    """
    inner_product = np.inner(arr1, arr2)
    outer_product = np.outer(arr1, arr2)
    return inner_product, outer_product