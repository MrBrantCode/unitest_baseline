"""
QUESTION:
In an array A of 0s and 1s, how many non-empty subarrays have sum S?
 
Example 1:
Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

 
Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.
"""

def count_subarrays_with_sum(A, S):
    ans = 0
    if S == 0:
        c = 0
        for i in range(len(A)):
            if A[i] == 0:
                c += 1
            else:
                c = 0
            ans += c
        return ans
    
    l = [-1]
    for i in range(len(A)):
        if A[i] == 1:
            l.append(i)
    l.append(len(A))
    
    ans = 0
    for i in range(1, len(l) - S):
        ans += (l[i] - l[i - 1]) * (l[i + S] - l[i + S - 1])
    
    return ans