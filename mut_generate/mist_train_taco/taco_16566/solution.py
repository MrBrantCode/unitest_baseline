"""
QUESTION:
min 

The tool min returns the minimum value along a given axis.

import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.min(my_array, axis = 0)         #Output : [1 0]
print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
print numpy.min(my_array, axis = None)      #Output : 0
print numpy.min(my_array)                   #Output : 0

By default, the axis value is None. Therefore, it finds the minimum over all the dimensions of the input array.    

 max 

The tool max returns the maximum value along a given axis.

import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.max(my_array, axis = 0)         #Output : [4 7]
print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
print numpy.max(my_array, axis = None)      #Output : 7
print numpy.max(my_array)                   #Output : 7

By default, the axis value is None. Therefore, it finds the maximum over all the dimensions of the input array.    

Task  

You are given a 2-D array with dimensions $N$X$\mbox{M}$. 

Your task is to perform the min function over axis $\mbox{I}$ and then find the max of that.

Input Format

The first line of input contains the space separated values of $N$ and $\mbox{M}$. 

The next $N$ lines contains $\mbox{M}$ space separated integers.

Output Format

Compute the min along axis $\mbox{I}$ and then print the max of that result. 

Sample Input
4 2
2 5
3 7
1 3
4 0

Sample Output
3

Explanation

The min along axis $\mbox{I}$ = $[2,3,1,0]$ 

The max of $[2,3,1,0]$ = $3$
"""

import numpy as np

def find_max_of_min_along_axis(arr, axis=1):
    """
    Computes the minimum values along the specified axis of the input array,
    and then returns the maximum value among those minimum values.

    Parameters:
    arr (numpy.ndarray): A 2-D numpy array.
    axis (int): The axis along which to compute the minimum (default is 1).

    Returns:
    int: The maximum value of the minimum values computed along the specified axis.
    """
    min_values = np.min(arr, axis=axis)
    max_of_min = np.max(min_values)
    return max_of_min