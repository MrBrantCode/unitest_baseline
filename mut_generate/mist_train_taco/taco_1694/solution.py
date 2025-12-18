"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 
Roman has no idea, why this problem is called Stone. He also has no idea on how to solve the followong problem: given array of N integers A and a number K. During a turn the maximal value over all A_{i} is chosen, let's call it MAX. Then A_{i} = 
MAX - A_{i} is done for every 1 ≤ i ≤ N. Help Roman to find out how will the array look like after K turns.

------ Input ------ 

The numbers N and K are given in the first line of an input. Then N integers are given in the second line which denote the array A. 

------ Output ------ 

Output N numbers on a single line. It should be the array A after K turns.

------ Constraints ------ 

$1 ≤ N ≤ 10^{5}$
$0 ≤ K ≤ 10^{9}$

$A_{i} does not exceed 2 * 10^{9} by it's absolute value.$

----- Sample Input 1 ------ 
4 1
5 -1 7 0
----- Sample Output 1 ------ 
2 8 0 7
"""

def transform_array_after_k_turns(N, K, A):
    if K == 0:
        return A
    
    if K % 2 == 1:
        MAX = max(A)
        return [MAX - A[i] for i in range(N)]
    else:
        MIN = min(A)
        return [-MIN + A[i] for i in range(N)]