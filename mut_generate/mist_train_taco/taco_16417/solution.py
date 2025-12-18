"""
QUESTION:
Given three sorted arrays A[] of size P, B[] of size Q and C[] of size R.Find a number X such that when  3 elements i, j and k are chosen from A, B and C respectively,then X=max(abs(A[i] – B[j]), abs(B[j] – C[k]), abs(C[k] – A[i])) is minimized. Here abs() indicates absolute value.
Example 1:
Input: 
P=3
A[] = {1, 4, 10}
Q=3
B[] = {2, 15, 20}
R=2
C[] = {10, 12}
Output:
5
Explanation:
We take 10 from A, 15 from B and
10 from C, so,
X=max(abs(10-15),abs(15-12),abs(10-10))
which gives X=18
Example 2:
Input: 
P=3
A[] = {20, 24, 100}
Q=5
B[] = {2, 19, 22, 79, 800}
R=5
C[] = {10, 12, 23, 24, 119}
Output:
2
Explanation:
We take 24 from A,22 from B and 24 from C.X
=max(abs(24-22),max(abs(24-22),abs(24-24)))
which is 2.
Your Task:
You don't need to read input or print anything.Your task is to complete the function findClosest() which takes P,Q,R,A[],B[],C[] as input parameters and returns the minimum X where X=max(abs(A[i]-B[j]),max(abs(A[i]-C[k]),abs(B[j]-C[k]))).
Expected Time Complexity:O(P+Q+R)
Expected Auxillary Space:O(1)
Constraints:
1<=P,Q,R<=10^{4}
1<=A[i],B[j],C[k]<=10^{6 }where 0<=i<P , 0<=j<Q , 0<=k<R
"""

def find_min_max_abs_diff(A, B, C):
    i, j, k = 0, 0, 0
    l1, l2, l3 = len(A), len(B), len(C)
    ans = float('inf')
    
    while i < l1 and j < l2 and k < l3:
        temp = max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
        if temp < ans:
            ans = temp
        
        if A[i] <= B[j] and A[i] <= C[k]:
            i += 1
        elif B[j] <= A[i] and B[j] <= C[k]:
            j += 1
        else:
            k += 1
    
    return ans