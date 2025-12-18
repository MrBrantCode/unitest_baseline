"""
QUESTION:
sum    

The sum tool returns the sum of array elements over a given axis.  

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.sum(my_array, axis = 0)         #Output : [4 6]
print numpy.sum(my_array, axis = 1)         #Output : [3 7]
print numpy.sum(my_array, axis = None)      #Output : 10
print numpy.sum(my_array)                   #Output : 10

By default, the axis value is None. Therefore, it performs a sum over all the dimensions of the input array.

prod

The prod tool returns the product of array elements over a given axis.  

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.prod(my_array, axis = 0)            #Output : [3 8]
print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
print numpy.prod(my_array, axis = None)         #Output : 24
print numpy.prod(my_array)                      #Output : 24

By default, the axis value is None. Therefore, it performs the product over all the dimensions of the input array.

Task  

You are given a 2-D array with dimensions $N$X$\mbox{M}$. 

Your task is to perform the $\textit{sum}$ tool over axis $\mbox{o}$ and then find the $\textit{product}$ of that result.

Input Format

The first line of input contains space separated values of $N$ and $\mbox{M}$. 

The next $N$ lines contains $\mbox{M}$ space separated integers.

Output Format

Compute the sum along axis $\mbox{o}$. Then, print the product of that sum. 

Sample Input
2 2
1 2
3 4

Sample Output
24

Explanation

The sum along axis $\mbox{o}$ = [$\begin{array}{c}A\end{array}$ $\boldsymbol{6}$] 

The product of this sum = $24$
"""

import numpy as np

def compute_sum_product(array, axis=0):
    """
    Computes the sum of the array elements along the specified axis and then returns the product of that sum.

    Parameters:
    array (numpy.ndarray): A 2-D numpy array.
    axis (int, optional): The axis along which to perform the sum operation. Default is 0.

    Returns:
    int: The product of the sum of the array elements along the specified axis.
    """
    sum_result = np.sum(array, axis=axis)
    product_result = np.prod(sum_result)
    return product_result