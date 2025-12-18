"""
QUESTION:
Given two positive numbers X and Y, check if Y is a power of X or not.
 
Example 1:
Input:
X = 2, Y = 8
Output:
1
Explanation:
2^{3} is equal to 8.
 
Example 2:
Input:
X = 1, Y = 8
Output:
0
Explanation:
Any power of 1 is not 
equal to 8.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function isPowerOfAnother() which takes an integer and returns 1 if y is the power of x, else return 0.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints: 
1 <= x <= 10^{3}
1 <= y <= 10^{8}
"""

from math import log

def is_power_of_another(X, Y):
    if X == 0 or X == 1:
        return 0
    else:
        m = log(Y, X)
        m = round(m)
        if X ** m == Y:
            return 1
        return 0