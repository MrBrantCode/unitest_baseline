"""
QUESTION:
Design a function named `fiveD_to_twoD` that takes a 5D array as input, represented by five dimensions: h blocks, t blocks, p layers, m horizontal lines, and n vertical lines, and returns a 2D matrix representation of the input array. The function should reduce the five dimensions into two dimensions by merging the first three dimensions into one.
"""

import numpy as np

def fiveD_to_twoD(fiveD_mat):
   #convert to numpy array for easier manipulation
   numpy_fiveD = np.array(fiveD_mat)
   #combine all dimensions into two
   twoD_mat = numpy_fiveD.reshape(-1, numpy_fiveD.shape[-1])
   return twoD_mat