"""
QUESTION:
You are given an array A of N integers and an integer K, and your task is to find the total number of cuts that you can make such that for each cut these two conditions are satisfied
1. A cut divides an array into two parts equal or unequal length (non-zero).
2. Sum of the largest element in the left part and the smallest element in the right part is greater than or equal to K.
Example 1:
Input:
N=3
K=3
A[]={1,2,3}
Output:
2
Explanation:
Two ways in which array is divided to satisfy above conditions are:
{1} and {2,3} -> 1+2>=3(satisfies the condition)
{1,2} and {3} -> 2+3>=3(satisfies the condition)
Example 2:
Input:
N=5
K=5
A[]={1,2,3,4,5}
Output:
3
Explanation:
{1,2} and {3,4,5} -> 2+3>=5
{1,2,3} and {4,5} -> 3+4>=5
{1,2,3,4} and {5} -> 4+5>=5
Your Task:
You don't need to read input or print anything. Your task is to complete the function totalCuts() which takes two integers N, K, and an array A of size N as input parameters, and returns an integer representing the total number of cuts that satisfy both conditions.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 <= N <= 10^6
0 <= K <= 10^6
0 <= A[i] <= 10^6
"""

from typing import List
import sys

def total_cuts(N: int, K: int, A: List[int]) -> int:
    c = 0
    mi = [0] * N
    ma = [0] * N
    miv = sys.maxsize
    mav = -sys.maxsize - 1
    
    # Fill the maximum values from the left to the right
    for i in range(N):
        mav = max(mav, A[i])
        ma[i] = mav
    
    # Fill the minimum values from the right to the left
    for i in range(N - 1, -1, -1):
        miv = min(miv, A[i])
        mi[i] = miv
    
    # Count the valid cuts
    for i in range(N - 1):
        if ma[i] + mi[i + 1] >= K:
            c += 1
    
    return c