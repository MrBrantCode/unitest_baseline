"""
QUESTION:
You are given two arrays A and B of length N. Let S be the set of integers from 1 to N. Can you find the maximum possible value of (A_{i1}+A_{i2}+...+A_{ik})^{2}+(B_{i1}+B_{i2}+...+B_{ik})^{2} where {i1,i2...ik} is a non-empty subset of S?

Input Format 

The first line contains a single integer T, denoting the number of test cases. 

T testcases follow, each test case given in following format.  

N  
A1 A2 ... AN  
B1 B2 ... BN  

Output Format 

For each test case, output the maximum possible value in one line.  

Constraints 

1 <= T <= 10 

1 <= N <= 1000 

-10^{6} <= A_{i}, B_{i} <= 10^{6}  

Sample Input  

1  
2  
-1 5  
4 -5  

Sample Output  

50

Explanation 

All possible non-empty subsets for N = 2 of S = {1,2} are {1}, {2} and {1,2}. The maximum possible values of the above equation now are 

(-1)^{2} + (4)^{2} = 17  
(5)^{2} + (-5)^{2} = 50  
(-1 + 5)^{2} + (4 - 5)^{2} = 17

hence 50. 

Timelimits

Timelimits for this challenge can be seen here
"""

from math import atan2

def max_subset_sum_square(A, B):
    vs = list(zip(A, B))
    vs = sorted(vs, key=lambda v: atan2(v[1], v[0]))
    best = 0
    
    for i in range(len(vs)):
        u = vs[i]
        l = u[0] * u[0] + u[1] * u[1]
        
        for v in (vs + vs)[i + 1:i + len(vs)]:
            tmpU = (u[0] + v[0], u[1] + v[1])
            tmpL = tmpU[0] * tmpU[0] + tmpU[1] * tmpU[1]
            if tmpL >= l:
                u = tmpU
                l = tmpL
        
        if l > best:
            best = l
        
        u = vs[i]
        l = u[0] * u[0] + u[1] * u[1]
        
        for v in reversed((vs + vs)[i + 1:i + len(vs)]):
            tmpU = (u[0] + v[0], u[1] + v[1])
            tmpL = tmpU[0] * tmpU[0] + tmpU[1] * tmpU[1]
            if tmpL >= l:
                u = tmpU
                l = tmpL
        
        if l > best:
            best = l
    
    return best