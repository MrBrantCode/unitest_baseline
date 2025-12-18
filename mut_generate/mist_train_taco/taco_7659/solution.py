"""
QUESTION:
Watson gives four 3-dimensional points to Sherlock and asks him if they all lie in the same plane. Your task here is to help Sherlock.   

Input Format 

First line contains T, the number of testcases. 

Each test case consists of four lines. Each line contains three integers, denoting x_{i} y_{i} z_{i}.   

Output Format 

For each test case, print YES or NO whether all four points lie in same plane or not, respectively.  

Constraints 

1 ≤ T ≤ 10^{4} 

-10^{3} ≤ x_{i},y_{i},z_{i} ≤ 10^{3}  

Sample Input

1
1 2 0
2 3 0
4 0 0
0 0 0

Sample Output

YES

Explanation 

All points have z_{i} = 0, hence they lie in the same plane, and output is YES
"""

def are_points_coplanar(points):
    A, B, C, D = points
    
    # Calculate vectors AB, AC, and AD
    AB = [B[i] - A[i] for i in range(3)]
    AC = [C[i] - A[i] for i in range(3)]
    AD = [D[i] - A[i] for i in range(3)]
    
    # Calculate the volume of the parallelepiped formed by AB, AC, and AD
    V = AB[0] * (AC[1] * AD[2] - AC[2] * AD[1])
    V += AB[1] * (AC[0] * AD[2] - AC[2] * AD[0])
    V += AB[2] * (AC[0] * AD[1] - AC[1] * AD[0])
    
    # If the volume is zero, the points are coplanar
    return 'YES' if V == 0 else 'NO'