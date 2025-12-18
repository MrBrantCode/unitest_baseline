"""
QUESTION:
=====Function Descriptions=====
floor
The tool floor returns the floor of the input element-wise.
The floor of x is the largest integer i where i≤x.

import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.floor(my_array)         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]

ceil
The tool ceil returns the ceiling of the input element-wise.
The ceiling of x is the smallest integer i where i≥x.

import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.ceil(my_array)          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]

rint
The rint tool rounds to the nearest integer of input element-wise.

import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.rint(my_array)          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]

=====Problem Statement=====
You are given a 1-D array, A. Your task is to print the floor, ceil and rint of all the elements of A.

=====Input Format=====
A single line of input containing the space separated elements of array A.

=====Output Format=====
On the first line, print the floor of A.
On the second line, print the ceil of A.
On the third line, print the rint of A.
"""

import numpy as np

def process_array(A: np.ndarray) -> tuple:
    """
    Processes the input array to compute the floor, ceil, and rint of each element.

    Parameters:
    A (np.ndarray): A 1-D numpy array of floating-point numbers.

    Returns:
    tuple: A tuple containing three numpy arrays:
           - The first element is the floor of the input array.
           - The second element is the ceil of the input array.
           - The third element is the rint of the input array.
    """
    floor_A = np.floor(A)
    ceil_A = np.ceil(A)
    rint_A = np.rint(A)
    
    return floor_A, ceil_A, rint_A