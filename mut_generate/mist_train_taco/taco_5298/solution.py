"""
QUESTION:
An extension of a complex number is called a quaternion. It is a convenient number that can be used to control the arm of a robot because it is convenient for expressing the rotation of an object. Quaternions are $ using four real numbers $ x $, $ y $, $ z $, $ w $ and special numbers (extended imaginary numbers) $ i $, $ j $, $ k $. It is expressed as x + yi + zj + wk $. The sum of such quaternions is defined as:

$ (x_1 + y_1 i + z_1 j + w_1 k) + (x_2 + y_2 i + z_2 j + w_2 k) = (x_1 + x_2) + (y_1 + y_2) i + (z_1 + z_2) j + (w_1 + w_2) k $

On the other hand, the product between 1, $ i $, $ j $, and $ k $ is given as follows.

<image>


This table represents the product $ AB $ of two special numbers $ A $ and $ B $. For example, the product $ ij $ of $ i $ and $ j $ is $ k $, and the product $ ji $ of $ j $ and $ i $ is $ -k $.

The product of common quaternions is calculated to satisfy this relationship. For example, the product of two quaternions, $ 1 + 2i + 3j + 4k $ and $ 7 + 6i + 7j + 8k $, is calculated as follows:

$ (1 + 2i + 3j + 4k) \ times (7 + 6i + 7j + 8k) = $
$ 7 + 6i + 7j + 8k $
$ + 14i + 12i ^ 2 + 14ij + 16ik $
$ + 21j + 18ji + 21j ^ 2 + 24jk $
$ + 28k + 24ki + 28kj + 32k ^ 2 $

By applying the table above

$ = -58 + 16i + 36j + 32k $

It will be.

Two quaternions ($ x_1 + y_1 i + z_1 j + w_1 k $) and ($) where the four coefficients $ x $, $ y $, $ z $, $ w $ are integers and not all zeros x_2 + y_2 i + z_2 j + w_2 k $), and the product is ($ x_3 + y_3 i + z_3 j + w_3 k $), $ x_3 $, $ y_3 $, $ z_3 $, $ Create a program that outputs w_3 $.



input

Given multiple datasets. The end of the input is indicated by a single line of zeros. Each dataset is given in the following format:

$ n $
$ data_1 $
$ data_2 $
::
$ data_n $


The first line gives the number of pairs of quaternions to process $ n $ ($ n \ leq 10 $). The following $ n $ line is given the $ i $ th quaternion pair of information $ data_i $ in the following format:

$ x_1 $ $ y_1 $ $ z_1 $ $ w_1 $ $ x_2 $ $ y_2 $ $ z_2 $ $ w_2 $

All coefficients given should be -1000 or more and 1000 or less. The number of datasets does not exceed 50.

output

Prints the product of a given set of quaternions for each dataset.

Example

Input

2
1 2 3 4 7 6 7 8
5 6 7 8 3 2 3 4
0


Output

-58 16 36 32
-50 32 28 48
"""

def quaternion_product(x1, y1, z1, w1, x2, y2, z2, w2):
    """
    Calculate the product of two quaternions.

    Parameters:
    x1, y1, z1, w1: int
        Coefficients of the first quaternion.
    x2, y2, z2, w2: int
        Coefficients of the second quaternion.

    Returns:
    tuple
        A tuple (x3, y3, z3, w3) representing the coefficients of the resulting quaternion.
    """
    x3 = x1 * x2 - y1 * y2 - z1 * z2 - w1 * w2
    y3 = x1 * y2 + x2 * y1 + z1 * w2 - z2 * w1
    z3 = x1 * z2 - y1 * w2 + x2 * z1 + y2 * w1
    w3 = x1 * w2 + y1 * z2 - y2 * z1 + x2 * w1
    
    return (x3, y3, z3, w3)