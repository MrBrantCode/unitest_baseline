"""
QUESTION:
Basic mathematical functions operate element-wise on arrays. They are available both as operator overloads and as functions in the NumPy module. 

import numpy

a = numpy.array([1,2,3,4], float)
b = numpy.array([5,6,7,8], float)

print a + b                     #[  6.   8.  10.  12.]
print numpy.add(a, b)           #[  6.   8.  10.  12.]

print a - b                     #[-4. -4. -4. -4.]
print numpy.subtract(a, b)      #[-4. -4. -4. -4.]

print a * b                     #[  5.  12.  21.  32.]
print numpy.multiply(a, b)      #[  5.  12.  21.  32.]

print a / b                     #[ 0.2         0.33333333  0.42857143  0.5       ]
print numpy.divide(a, b)        #[ 0.2         0.33333333  0.42857143  0.5       ]

print a % b                     #[ 1.  2.  3.  4.]
print numpy.mod(a, b)           #[ 1.  2.  3.  4.]

print a**b                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print numpy.power(a, b)         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]

Task  

You are given two integer arrays, $\mbox{A}$ and $\mbox{B}$ of dimensions $N$X$\mbox{M}$. 

Your task is to perform the following operations:

Add ($\mbox{A}$ + $\mbox{B}$)   
Subtract ($\mbox{A}$ - $\mbox{B}$)  
Multiply ($\mbox{A}$ * $\mbox{B}$)   
Integer Division ($\mbox{A}$ / $\mbox{B}$)  
Mod ($\mbox{A}$ % $\mbox{B}$)  
Power ($\mbox{A}$ ** $\mbox{B}$)

Note 

There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.  

Input Format

The first line contains two space separated integers, $N$ and $\mbox{M}$. 

The next $N$ lines contains $\mbox{M}$ space separated integers of array $\mbox{A}$. 

The following $N$ lines contains $\mbox{M}$ space separated integers of array $\mbox{B}$.  

Output Format

Print the result of each operation in the given order under Task.

Sample Input
1 4
1 2 3 4
5 6 7 8

Sample Output
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 

Use // for division in Python 3.
"""

import numpy as np

def perform_array_operations(A, B):
    """
    Perform element-wise operations on two 2D NumPy arrays.

    Parameters:
    A (numpy.ndarray): The first 2D input array.
    B (numpy.ndarray): The second 2D input array.

    Returns:
    dict: A dictionary containing the results of the operations:
          'add', 'subtract', 'multiply', 'divide', 'mod', 'power'.
    """
    results = {
        'add': np.add(A, B),
        'subtract': np.subtract(A, B),
        'multiply': np.multiply(A, B),
        'divide': A // B,
        'mod': np.mod(A, B),
        'power': np.power(A, B)
    }
    return results