"""
QUESTION:
Implement the `hist_matching` function to modify the pixel values of an input image `im` based on the cumulative distribution functions (CDFs) `c` and `c_t` of the input and a template image. The function should take three parameters: `c` (CDF of input image), `c_t` (CDF of template image), and `im` (input image as 2D numpy ndarray). It should return the modified pixel values of the input image after applying the histogram matching algorithm.
"""

import numpy as np

def hist_matching(c, c_t, im):
    # Compute the mapping function from c to c_t
    mapping = np.interp(c, c_t, range(256))
    
    # Apply the mapping to the input image
    modified_im = mapping[im]
    
    return modified_im