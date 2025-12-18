"""
QUESTION:
Given two integers N and M  you have to find out an integer which is a power of M and is nearest to N.
Note: If there are multiple answers possible to, print the greatest number possible.
 
Example 1:
Input:
N = 6, M = 3
Output:
9
Explanation:
Both 3 (3^{1}) and 9 (3^{2}) are equally
near to 6. But 9 is greater,
so the Output is 9.
Example 2:
Input:
N = 3, M = 2
Output:
4
Explanation:
Both 2 (2^{1}) and 4 (2^{2}) are equally
near to 3. But 4 is greater,
so the Output is 4.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function nearestPower() which takes 2 Integers N and M as input and returns the answer.
 
Expected Time Complexity: O(max(log(N),log(M)))
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N,M <= 10^{9}
"""

from math import log

def nearest_power(N, M):
    if N == M:
        return 1
    thres = log(N) // log(M)
    res1 = abs(N - M ** thres)
    res2 = abs(N - M ** (thres + 1))
    if res1 == res2:
        return int(M ** (thres + 1))
    elif res1 > res2:
        return int(M ** (thres + 1))
    else:
        return int(M ** thres)